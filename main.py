"""The One-Line Laugh — entry program.

Writes exactly one funny line (a single sentence, well under the
200-character gate) to /output/entry.txt, with no trailing newline.

Stdlib only: the grader's Python image has no third-party packages.
Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "The fastest way to get a reply from customer service is to post "
    "about them publicly, which is just blackmail with better branding."
)


def main():
    data = LINE.encode("utf-8")
    # Fail loudly instead of ever writing an entry the gate refuses:
    # the gate needs UTF-8 text of 1 to 200 characters, not only whitespace.
    if not 1 <= len(data.decode("utf-8")) <= 200 or not LINE.strip():
        raise ValueError("entry line outside the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
