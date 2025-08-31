#!/bin/sh
# Check NVIDIA GPU status without waking it up if it's sleeping 😴.

exec cat /proc/driver/nvidia/gpus/0000:01:00.0/power
