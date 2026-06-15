import sqlite3
import json
import os
import time

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'osm_cache.db')
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


def _conn():
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute('''CREATE TABLE IF NOT EXISTS cache (
        key TEXT PRIMARY KEY,
        response TEXT,
        ts INTEGER
    )''')
    conn.commit()
    return conn


def get_cache(key: str, max_age: int = None):
    try:
        conn = _conn()
        cur = conn.execute('SELECT response, ts FROM cache WHERE key=?', (key,))
        row = cur.fetchone()
        conn.close()
        if not row:
            return None
        resp_text, ts = row
        if max_age is not None and int(time.time()) - ts > max_age:
            return None
        return json.loads(resp_text)
    except Exception:
        return None


def set_cache(key: str, response_obj):
    try:
        conn = _conn()
        resp_text = json.dumps(response_obj, ensure_ascii=False)
        ts = int(time.time())
        conn.execute('INSERT OR REPLACE INTO cache(key, response, ts) VALUES (?, ?, ?)', (key, resp_text, ts))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False
