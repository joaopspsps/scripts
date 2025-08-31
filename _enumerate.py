#!/usr/bin/env python3
"""Group and sequence related files by changing their names.

For example::

    > ls
    foo
    bar
    quux
    > ,enumerate foo bar quux
    > ls
    vV6TtlMk4PvvLjcm_0_foo
    vV6TtlMk4PvvLjcm_1_bar
    vV6TtlMk4PvvLjcm_2_quux
"""

import argparse
import random
import string
from pathlib import Path
from string import Template


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=Path, nargs="+", help="Files to process")
    parser.add_argument(
        "-t",
        dest="template",
        type=Template,
        default="${random}_${n}_${name}",
        help="Template used for the new filename (default: '%(default)s'). Available placeholders: `random` (random string for grouping), `n` (number for sequencing), and `name` (original filename).",
    )
    parser.add_argument(
        "-l",
        dest="len",
        type=int,
        default=16,
        help="Length of the random string (default: %(default)s)",
    )
    parser.add_argument(
        "-n",
        dest="ignore_n",
        action="store_true",
        help="Ignore `n` in the template (i.e., for when there's no sequencing between files)",
    )
    args = parser.parse_args()

    random_string = "".join(
        random.sample(string.ascii_letters + string.digits, args.len)
    )

    for i, src in enumerate(args.files):
        new_name = args.template.substitute(
            random=random_string, n="" if args.ignore_n else i, name=src.name
        )
        dst = src.with_name(new_name)
        src.rename(dst)


if __name__ == "__main__":
    main()
