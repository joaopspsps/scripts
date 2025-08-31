#!/bin/sh
# Flash screen by briefly turning off brightness.

b="$(brightnessctl -q get)"
brightnessctl -q set 0
brightnessctl -q set "$b"
