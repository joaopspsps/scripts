#!/bin/sh
# Test microphone input visually.
#
# Dependencies:
#   - alsa-utils for arecord

exec arecord -vvv -f dat /dev/null "$@"
