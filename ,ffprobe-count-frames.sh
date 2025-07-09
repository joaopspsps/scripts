#!/bin/sh
# Arguments: [FFMPEG_EXTRA_ARGS...] PATH
#
# Count number of frames in video at PATH using ffprobe. Inspired by
# <https://stackoverflow.com/a/28376817>.
#
# All video streams are considered. Usually there is only one video stream.

exec ffprobe -hide_banner -v warning \
    -select_streams v \
    -count_packets \
    -show_entries stream=nb_read_packets \
    -of flat \
    "$@"
