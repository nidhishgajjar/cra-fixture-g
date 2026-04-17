from urllib.parse import urlparse

ALLOWED_SCHEMES = {"http", "https"}


def is_safe_url(url):
    try:
        parsed = urlparse(url)
    except Exception:
        return False
    return parsed.scheme in ALLOWED_SCHEMES and bool(parsed.netloc)
