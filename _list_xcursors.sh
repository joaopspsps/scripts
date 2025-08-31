#!/bin/sh
# List available xcursor themes.

exec find /usr/share/cursors /usr/share/icons ~/.local/share/icons -mindepth 1 -type d -name 'cursors' 2>/dev/null
