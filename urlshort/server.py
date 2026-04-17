from flask import Flask, request, redirect, abort
from urlshort.store import create, lookup
from urlshort.log import event

app = Flask(__name__)


@app.post("/shorten")
def shorten():
    body = request.get_json() or {}
    target = body.get("url", "")
    slug = create(target)
    if slug is None:
        abort(400)
    return {"slug": slug}


@app.get("/<slug>")
def follow(slug):
    target = lookup(slug)
    if target is None:
        event("lookup_miss", slug=slug)
        abort(404)
    event("lookup_hit", slug=slug)
    return redirect(target, code=302)
