import re
import sys
import fileinput


def process_vtt():
    for line in fileinput.input("-"):
        line = line.strip()

        # Remove <v> tags from text lines
        line = re.sub(r"</?v[^>]*>", "", line)

        # Remove &amp; entities text lines
        line = re.sub(r"&amp;", "&", line)

        # Remove UUID lines
        if re.match(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(/[0-9]+-[0-9]+)?",
            line,
        ):
            continue

        print(line)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Removes markup inserted by Microsoft Teams.")
        print("")
        print("Usage: python clean_vtt.py")
        sys.exit(1)

    process_vtt()
