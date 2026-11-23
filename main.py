"""One-Line Roast: The Gadget You Use Every Day — make.fun entry
(account A / overtheraa).

Writes a single original roast line about the phone I use every day to
entry.txt inside $MAKEFUN_OUTPUT_DIR (default /output). Deterministic,
stdlib only, no network, no model calls, no file reads outside this repo.
"""

import os

ROAST = (
    "My phone's 128 GB is 127 GB of screenshots I swore I'd read later "
    "and 1 GB of food I already ate."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
MAX_CHARS = 200


def main() -> int:
    if not 1 <= len(ROAST) <= MAX_CHARS:
        raise ValueError(f"roast is {len(ROAST)} chars, gate needs 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
