import re
import sys
import fileinput


def process_vtt(offset):
    for line in fileinput.input("-"):
        line = line.strip()

        if re.match(r"^\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+$", line):
            # Process timestamp lines and add the offset
            start, arrow, end = line.partition(" --> ")
            start_time, end_time = map(parse_timestamp, (start, end))
            start_time += offset
            end_time += offset
            new_timestamp = (
                format_timestamp(start_time) + " --> " + format_timestamp(end_time)
            )
            print(new_timestamp)
        else:
            print(line)


def parse_timestamp(timestamp):
    h, m, s = map(float, re.split(r"[:,]", timestamp))
    return h * 3600 + m * 60 + s


def format_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Offsets times by a number of seconds.")
        print("")
        print("Usage: python offset_vtt.py <offset>")
        sys.exit(1)

    offset = float(sys.argv[1])
    process_vtt(offset)
