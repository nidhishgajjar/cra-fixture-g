import json, sys, time


def event(action, **fields):
    record = {"ts": time.time(), "action": action, **fields}
    sys.stdout.write(json.dumps(record) + "\n")
    sys.stdout.flush()
