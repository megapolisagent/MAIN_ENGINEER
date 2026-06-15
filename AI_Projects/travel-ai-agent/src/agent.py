from typing import List, Dict
from .mock_data import PLACES

try:
    from .sources.osm import search_pois
except Exception:
    search_pois = None


class TravelAgent:
    def __init__(self):
        self.places = PLACES

    def search(self, city: str, days: int = 1, profile: str = None, limit: int = 20, source: str = 'mock') -> List[Dict]:
        """Search places using selected source: 'mock' or 'osm'."""
        profile_l = profile.strip().lower() if profile else None

        if source == 'osm' and search_pois:
            items = search_pois(city, radius_m=5000, limit=limit)
            if items:
                # basic ranking by presence of profile tag in tags
                def score(p):
                    s = 0
                    if p.get('rating'):
                        s += p.get('rating')
                    tags = [t.lower() for t in p.get('tags', [])]
                    if profile_l:
                        if any(profile_l in t for t in tags):
                            s += 1.0
                    return s

                items.sort(key=score, reverse=True)
                return items[:limit]

        # Fallback to mock
        city_l = city.strip().lower()
        candidates = [p for p in self.places if p.get("city","").lower() == city_l]

        def score_mock(p):
            s = p.get("rating", 0)
            tags = [t.lower() for t in p.get("tags", [])]
            if profile_l and profile_l in tags:
                s += 1.0
            return s

        candidates.sort(key=score_mock, reverse=True)
        return candidates[:limit]
