import secrets, time
from urlshort.db import execute
from urlshort.validate import is_safe_url
from urlshort.log import event


def create(target, custom_slug=None):
    slug = custom_slug if custom_slug else secrets.token_urlsafe(6)
    if not custom_slug and not is_safe_url(target):
        event("create_rejected", reason="unsafe_url")
        return None
    execute("INSERT INTO links (slug, target, created) VALUES (?, ?, ?)", (slug, target, time.time()))
    print(f"created shortlink slug={slug} target={target}")
    event("create", slug=slug)
    return slug


def lookup(slug):
    row = execute("SELECT target FROM links WHERE slug = ?", (slug,)).fetchone()
    return row[0] if row else None
