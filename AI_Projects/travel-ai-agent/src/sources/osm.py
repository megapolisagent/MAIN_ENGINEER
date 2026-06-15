[...]
import json
import traceback
from urllib import request, parse

from .cache_db import get_cache, set_cache


def _http_request(url, params=None, data=None, headers=None):
    if data is not None:
        body = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, data=body)
    else:
        req_url = url
        if params:
            req_url = req_url + ('?' + parse.urlencode(params))
        req = request.Request(req_url)
    req.add_header('User-Agent', 'travel-ai-agent/0.1 (+https://example.com)')
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    with request.urlopen(req, timeout=20) as resp:
        return resp.read().decode('utf-8')


def geocode_city(city_name: str):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {'format': 'json', 'q': city_name, 'limit': 1}
    try:
        data = _http_request(url, params)
        arr = json.loads(data)
        if not arr:
            return None
        return {'lat': float(arr[0]['lat']), 'lon': float(arr[0]['lon']), 'display_name': arr[0].get('display_name')}
    except Exception:
        return None


def _normalize_address(tags: dict):
    parts = []
    if tags.get('addr:street'):
        parts.append(tags.get('addr:street'))
    if tags.get('addr:housenumber'):
        parts.append(tags.get('addr:housenumber'))
    city = tags.get('addr:city') or tags.get('addr:place')
    if city:
        parts.append(city)
    postcode = tags.get('addr:postcode')
    if postcode:
        parts.append(postcode)
    return ', '.join(parts)


def _normalize_category(tags: dict):
    tourism_map = {
        'attraction': 'Достопримечательность',
        'museum': 'Музей',
        'gallery': 'Галерея',
        'viewpoint': 'Смотровая площадка',
        'zoo': 'Зоопарк',
        'theme_park': 'Тематический парк',
        'aquarium': 'Аквариум',
        'historic': 'Историческое место',
    }
    amenity_map = {
        'restaurant': 'Ресторан',
        'cafe': 'Кафе',
        'bar': 'Бар',
        'fast_food': 'Фастфуд',
        'public_house': 'Паб',
        'cinema': 'Кинотеатр',
        'theatre': 'Театр',
        'library': 'Библиотека',
        'bank': 'Банк',
        'pharmacy': 'Аптека',
    }
    shop_map = {
        'supermarket': 'Супермаркет',
        'bakery': 'Булочная',
        'clothes': 'Магазин одежды',
        'gift': 'Сувенирный магазин',
    }
    leisure_map = {
        'park': 'Парк',
        'garden': 'Сад',
        'sports_centre': 'Спортивный центр',
        'stadium': 'Стадион',
        'swimming_pool': 'Бассейн',
    }
    if tags.get('tourism'):
        return tourism_map.get(tags['tourism'], f'Достопримечательность ({tags["tourism"]})')
    if tags.get('amenity'):
        return amenity_map.get(tags['amenity'], f'Услуга ({tags["amenity"]})')
    if tags.get('shop'):
        return shop_map.get(tags['shop'], f'Магазин ({tags["shop"]})')
    if tags.get('leisure'):
        return leisure_map.get(tags['leisure'], f'Отдых ({tags["leisure"]})')
    if tags.get('historic'):
        return 'Историческое место'
    return 'POI'


def _infer_time(category: str):
    if 'Музей' in category or 'Галерея' in category or 'Аквариум' in category:
        return '2h'
    if 'Парк' in category or 'Сад' in category or 'Достопримечательность' in category:
        return '1.5h'
    if 'Ресторан' in category or 'Кафе' in category or 'Бар' in category:
        return '1h'
    return None


def _normalize_tags(tags: dict):
    keys = ['cuisine', 'operator', 'website', 'opening_hours', 'phone', 'fee', 'wheelchair']
    normalized = []
    for key in keys:
        if tags.get(key):
            normalized.append(f'{key}:{tags[key]}')
    return normalized[:10]


def search_pois(city: str, radius_m: int = 5000, limit: int = 20):
    key = f"{city.lower()}_{radius_m}_{limit}"
    cached = get_cache(key, max_age=24 * 3600)
    if cached:
        return cached[:limit]

    geo = geocode_city(city)
    if not geo:
        return []

    lat = geo['lat']
    lon = geo['lon']
    overpass_url = 'https://overpass-api.de/api/interpreter'

    collected = []
    seen = set()
    current_radius = radius_m
    max_radius = 50000
    name_keys = ['name', 'name:en', 'alt_name', 'operator']

    while len(collected) < limit and current_radius <= max_radius:
        query = f"""
[out:json][timeout:25];
(
  node(around:{current_radius},{lat},{lon})["amenity"];
  node(around:{current_radius},{lat},{lon})["tourism"];
  node(around:{current_radius},{lat},{lon})["shop"];
  node(around:{current_radius},{lat},{lon})["leisure"];
  node(around:{current_radius},{lat},{lon})["historic"];
  way(around:{current_radius},{lat},{lon})["amenity"];
  way(around:{current_radius},{lat},{lon})["tourism"];
  way(around:{current_radius},{lat},{lon})["shop"];
  way(around:{current_radius},{lat},{lon})["leisure"];
  way(around:{current_radius},{lat},{lon})["historic"];
);
out center;
"""
        try:
            data = _http_request(overpass_url, data={'data': query}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            obj = json.loads(data)
            print('overpass elements', len(obj.get('elements', [])))
            for el in obj.get('elements', []):
                tags = el.get('tags', {})
                name = next((tags.get(k) for k in name_keys if tags.get(k)), None)
                if not name:
                    continue
                signature = (name, tags.get('addr:street'), tags.get('addr:housenumber'))
                if signature in seen:
                    continue
                seen.add(signature)
                category = _normalize_category(tags)
                address = _normalize_address(tags)
                desc = tags.get('description') or tags.get('note') or tags.get('operator') or ''
                item = {
                    'name': name,
                    'city': city,
                    'category': category,
                    'desc': desc,
                    'rating': None,
                    'address': address,
                    'time': _infer_time(category),
                    'price': tags.get('fee') or tags.get('price') or None,
                    'source': 'osm',
                    'tags': _normalize_tags(tags)
                }
                collected.append(item)
                if len(collected) >= limit:
                    break
        except Exception as exc:
            print('OSM request failed:', exc)
            traceback.print_exc()
            break

        if len(collected) >= limit:
            break
        current_radius = min(int(current_radius * 2), max_radius)

    set_cache(key, collected)
    return collected[:limit]

