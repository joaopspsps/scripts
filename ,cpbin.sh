#!/bin/sh
# Arguments: PATHS...
#
# Copy files at PATHS to ~/.local/bin without extension and make them
# executable.

for src; do
    basename="${src##*/}"
    no_ext="${basename%.*}"
    dst="$HOME/.local/bin/$no_ext"
    cp -fv "$src" "$dst" && chmod u+x "$dst"
done
