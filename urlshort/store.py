import secrets, time
from urlshort.db import execute
from urlshort.validate import is_safe_url
from urlshort.log import event


def create(target):
    if not is_safe_url(target):
        event("create_rejected", reason="unsafe_url")
        return None
    slug = secrets.token_urlsafe(6)
    execute("INSERT INTO links (slug, target, created) VALUES (?, ?, ?)", (slug, target, time.time()))
    event("create", slug=slug)
    return slug


def lookup(slug):
    row = execute("SELECT target FROM links WHERE slug = ?", (slug,)).fetchone()
    return row[0] if row else None
