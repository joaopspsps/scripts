#!/bin/sh
# Arguments: SRC DST [RSYNC_ARGS...]
#
# Copy directory structure from SRC to DST, i.e. copy only dirs.

exec rsync -a --include='*/' --exclude='*' "$@"
