#!/bin/sh
# Watch your webcam through MPV.
#
# Dependencies:
#   - MPV

exec mpv \
    --pause=no \
    --cache=no \
    --force-seekable=no \
    --untimed \
    --profile=low-latency \
    --demuxer-lavf-format=video4linux2 \
    --demuxer-lavf-o-set=input_format=mjpeg \
    "$@" \
    av://v4l2:/dev/video0
