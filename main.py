"""make.fun entry: Your Week in One Line.

Writes the entry text to /output/entry.txt for the make.fun grader.
No network, no secrets, no files outside this repository.
"""
from pathlib import Path
ENTRY = 'Built a planet with no tenants, a pattern library with one chart, and a joke the Roomba laughed at.'
OUTPUT = Path("/output/entry.txt")
def write_entry() -> Path:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    return OUTPUT
def main() -> None:
    write_entry()
if __name__ == "__main__":
    main()
