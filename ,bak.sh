#!/bin/sh
# Arguments: PATHS...
#
# Create a backup for each file at PATHS. The backups will have the suffix
# `.bak`.

for arg; do
    [ -f "$arg" ] && cp -a "$arg" "$arg.bak"
done
