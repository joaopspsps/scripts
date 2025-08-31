#!/bin/sh
# Arguments: IMAGE_FILENAME DEGREES
#
# Rotate the image by DEGREES degrees clockwise using imagemagick. the
# original modification time is preserved.
#
# Dependencies:
#   - imagemagick

set -eu

image_filename="$1"
degrees="$2"

original_mtime="$(stat -c @%Y "$image_filename")"
magick "$image_filename" -rotate "$degrees" "$image_filename"
touch -d "$original_mtime" "$image_filename"
