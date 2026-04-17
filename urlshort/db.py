import sqlite3

_conn = sqlite3.connect(":memory:", check_same_thread=False)
_conn.execute("CREATE TABLE IF NOT EXISTS links (slug TEXT PRIMARY KEY, target TEXT NOT NULL, created REAL NOT NULL)")
_conn.commit()


def execute(sql, params=()):
    cur = _conn.execute(sql, params)
    _conn.commit()
    return cur
