import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.sources.cache_db import set_cache, get_cache


def run():
    k = 'unit_test_key'
    v = {'hello': 'world'}
    ok = set_cache(k, v)
    res = get_cache(k)
    print('set_ok=', ok)
    print('res=', res)


if __name__ == '__main__':
    run()
