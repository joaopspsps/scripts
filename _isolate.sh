#!/bin/sh
# Play quiet brown noise using sox.
#
# Thanks, mawww.

exec play "|sox -n -p synth brownnoise" vol 0.2 "$@"
