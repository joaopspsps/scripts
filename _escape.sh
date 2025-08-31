#!/bin/sh
# Escape special shell characters from stdin.

exec sed "s@\([ 	\"'()\{\}<>\$&\|\*\?!;]\)@\\\\\1@g"
