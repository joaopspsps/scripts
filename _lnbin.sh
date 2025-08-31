#!/bin/sh
# Arguments: PATHS...
#
# Softlink files at PATHS to ~/.local/bin without extension.

for src; do
    basename="${src##*/}"
    no_ext="${basename%.*}"
    dst="$HOME/.local/bin/$no_ext"
    ln -sfv "$(realpath "$src")" "$dst" && chmod u+x "$dst"
done
