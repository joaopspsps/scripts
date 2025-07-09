#!/usr/bin/env python3
"""Change foot terminal's opacity using OSC-11 control sequences."""

import argparse
import os
import sys

# NOTE: Change this to your terminal's background color
BACKGROUND_COLOR = "#050811"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "opacity",
        type=int,
        default=80,
        nargs="?",
        help="Target terminal opacity (between 0 and 100) (default: %(default)d)",
    )
    args = parser.parse_args()

    if args.opacity < 0:
        opacity = 0
    elif args.opacity > 100:
        opacity = 100
    else:
        opacity = args.opacity

    tty = os.ttyname(sys.stdout.fileno())

    with open(tty, "w") as f:
        f.write(f"\033]11;[{opacity}]{BACKGROUND_COLOR}")


if __name__ == "__main__":
    main()
