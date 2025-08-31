#!/bin/sh
# Arguments: CMD...
#
# Run CMD without internet access.

[ $# -gt 0 ] || exit 1

exec unshare -cn env "$@"
