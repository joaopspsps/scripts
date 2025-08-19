#!/usr/bin/env python3
"""Edit symlink targets using $EDITOR."""

import argparse
import shlex
import logging
import os
import subprocess
import sys
import tempfile
from pathlib import Path

logging.basicConfig(format="%(message)s", level=logging.INFO)
logger = logging.getLogger()

SEPARATOR = "\t"
EDITOR = os.environ.get("EDITOR", "vi")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    paths = parser.add_argument(
        "paths", type=Path, nargs="+", help="Paths to symlinks to edit"
    )
    args = parser.parse_args()

    pairs = {}
    for path in args.paths:
        if not path.is_symlink():
            logger.info("Ignoring non-symlink argument: %s", path)
            continue
        pairs[str(path)] = str(path.readlink())

    if not pairs:
        logger.info("No arguments remaining, exiting...")
        sys.exit(1)

    with tempfile.NamedTemporaryFile("w+t") as fp:
        for path, resolved_path in pairs.items():
            fp.write(f"{path}{SEPARATOR}{resolved_path}\n")

        fp.seek(0)
        subprocess.run(shlex.split(EDITOR) + [fp.name], check=True)

        for line in Path(fp.name).read_text().splitlines():
            path, edited_resolved_path = line.strip().split(SEPARATOR)

            if path not in pairs:
                logger.info("Ignoring undeclared: %s", path)
                continue

            original_resolved_path = pairs[path]
            if edited_resolved_path == original_resolved_path:
                logger.info("Ignoring unchanged: %s", path)
                continue

            path = Path(path)
            tmp = path.with_name(path.name + ".tmp")
            tmp.symlink_to(edited_resolved_path)
            tmp.replace(path)
