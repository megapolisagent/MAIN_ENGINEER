import urllib.request
import urllib.parse
import urllib.error
import json

q = '[out:json][timeout:25];node(around:5000,41.3825802,2.177073)[amenity];out;'
endpoints = [
    'https://overpass-api.de/api/interpreter',
    'https://lz4.overpass-api.de/api/interpreter',
    'https://overpass.kumi.systems/api/interpreter',
    'https://overpass.openstreetmap.ru/api/interpreter',
]

for endpoint in endpoints:
    print(f'--- Testing endpoint {endpoint} ---')
    print('--- GET request ---')
    try:
        url = endpoint + '?' + urllib.parse.urlencode({'data': q})
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'travel-ai-agent/0.1 (+https://example.com)')
        resp = urllib.request.urlopen(req, timeout=20)
        txt = resp.read().decode('utf-8')
        print('status', resp.status)
        print('content-type', resp.getheader('content-type'))
        obj = json.loads(txt)
        print('elements', len(obj.get('elements', [])))
    except urllib.error.HTTPError as e:
        print('code', e.code)
        print('headers', e.headers)
        print('body', e.read().decode('utf-8'))
    except Exception as e:
        print('error', e)

    print('\n--- POST request ---')
    try:
        data = urllib.parse.urlencode({'data': q}).encode('utf-8')
        req = urllib.request.Request(endpoint, data=data)
        req.add_header('User-Agent', 'travel-ai-agent/0.1 (+https://example.com)')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        resp = urllib.request.urlopen(req, timeout=20)
        txt = resp.read().decode('utf-8')
        print('status', resp.status)
        print('content-type', resp.getheader('content-type'))
        obj = json.loads(txt)
        print('elements', len(obj.get('elements', [])))
    except urllib.error.HTTPError as e:
        print('code', e.code)
        print('headers', e.headers)
        print('body', e.read().decode('utf-8'))
    except Exception as e:
        print('error', e)
