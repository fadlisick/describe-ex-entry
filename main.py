# describe-ex entry: a one-word verdict on an ex.
# The verdict below is the whole entry: one word, nothing else attached.
# The program drops it into entry.txt exactly as written, no newline added.

import os

VERDICT = "Lemon"
CHAR_LIMIT = 111
OUT_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_DIR = "/output"
FILE_NAME = "entry.txt"


def target_path():
    """Resolve where entry.txt goes: the harness dir, or /output."""
    chosen = os.environ.get(OUT_VAR)
    base = chosen if chosen else DEFAULT_DIR
    return os.path.join(base, FILE_NAME)


def validate(word):
    """A valid verdict is one word, non-blank, within the char limit."""
    if not word or not word.strip():
        raise SystemExit("verdict is blank")
    if len(word.split()) != 1:
        raise SystemExit("verdict must be exactly one word")
    if len(word) > CHAR_LIMIT:
        raise SystemExit("verdict is over the 111 character limit")
    return word


def emit(word):
    """Write the verdict and read it back to prove it landed intact."""
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        saved = handle.read()
    if saved != word:
        raise SystemExit("read-back mismatch in entry.txt")
    return path, len(saved.encode("utf-8"))


def main():
    word = validate(VERDICT)
    path, size = emit(word)
    print("entry.txt ready: %d bytes at %s" % (size, path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
