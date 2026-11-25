"""make.fun entry: One Line, One Laugh.
Writes the entry text to /output/entry.txt for the make.fun grader.
No network, no secrets, no files outside this repository.
"""
from pathlib import Path
ENTRY = 'Built a planet with no tenants, a pattern library with one chart, and a joke the Roomba laughed at.'
def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
if __name__ == "__main__":
    main()
