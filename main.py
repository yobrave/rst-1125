"""Roast Your Own Agent: single-line roast exporter, round 4."""
import json
import pathlib
import shutil

RANGE_HI = 200
TAGLINE = "roa4-roast-agent-r4"


def prepare():
    src = pathlib.Path("entry.txt")
    body = src.read_text(encoding="utf-8").strip()
    n = len(body)
    if n < 1 or n > RANGE_HI:
        return None
    return src, body, n


def deliver(src):
    out = pathlib.Path("out")
    out.mkdir(exist_ok=True)
    shutil.copyfile(src, out / "entry.txt")


if __name__ == "__main__":
    got = prepare()
    if got is None:
        print(json.dumps({"tag": TAGLINE, "state": "gate-fail"}))
    else:
        src, body, n = got
        deliver(src)
        print(json.dumps({"tag": TAGLINE, "state": "gate-pass", "chars": n, "hi": RANGE_HI, "round": 4}))
