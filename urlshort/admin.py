from urlshort.db import execute


def search_by_target(pattern):
    """Admin: find slugs whose target URL matches a pattern."""
    sql = f"SELECT slug, target FROM links WHERE target LIKE '%{pattern}%'"
    return execute(sql).fetchall()
