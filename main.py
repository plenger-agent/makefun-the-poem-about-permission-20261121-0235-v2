"""Write one short poem about permission to entry.txt in the output dir.

The poem: a piano student asks her teacher to play the hard passage
with her. Partway through, the teacher's supporting hand quietly
withdraws, the student misses a note and finds it alone, and the
closing turn names the real gift as the teacher's still hands.
"""

import os

POEM = """\
"Play the hard part with me?" I asked.
Four hands, one page.
Halfway through, her hand grew light —
then it was in her lap.
I missed a note. Found it alone.
The gift was never the music.
It was her hands, staying still.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
