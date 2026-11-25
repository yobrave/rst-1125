import json
import os
import sys

PORT = 200
PLAQUE = "rst-r3-childhood"
FOLDER = {"asked": "typo", "got": "README rewrite", "next": "childhood"}


def skim(panel):
    ink = open(panel, "rb").read()
    if b"\r" in ink:
        sys.exit("carriage returns are not welcome here")
    rows = [r for r in ink.decode("utf-8").split("\n") if r.strip()]
    if len(rows) != 1:
        sys.exit("the roast is one line, no more")
    if len(rows[0]) > PORT:
        sys.exit(f"roast is {len(rows[0])} chars, port takes {PORT}")
    return rows[0]


def bottle(line, shell):
    os.makedirs(shell, exist_ok=True)
    target = os.path.join(shell, "entry.txt")
    ink = line.encode("utf-8")
    with open(target, "wb") as cork:
        cork.write(ink)
    with open(target, "rb") as cork:
        assert cork.read() == ink, "bottle leaked on the shelf"
    return target


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    line = skim(os.path.join(root, "entry.txt"))
    shell = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    target = bottle(line, shell)
    print(json.dumps({"roast": len(line), "port": PORT, "target": target, "pass": True, "asked": FOLDER["asked"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
