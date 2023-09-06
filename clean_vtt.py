import re
import sys
import fileinput


def process_vtt():
    for line in fileinput.input("-"):
        line = line.strip()

        # Remove <v> tags from text lines
        line = re.sub(r"</?v[^>]*>", "", line)
        print(line)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Removes markup inserted by Microsoft Teams.")
        print("")
        print("Usage: python clean_vtt.py")
        sys.exit(1)

    process_vtt()
