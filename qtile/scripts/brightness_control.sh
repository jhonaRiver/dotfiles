#!/bin/bash

current_brightness=$(xrandr --verbose | grep -i brightness | awk '{ print $2 }')

case "$1" in
    "increase")
        new_brightness=$(echo "$current_brightness + 0.1" | bc)
        ;;
    "decrease")
        new_brightness=$(echo "$current_brightness - 0.1" | bc)
        ;;
    *)
        echo "Usage: $0 [increase|decrease]"
        exit 1
        ;;
esac

xrandr --output eDP-1 --brightness $new_brightness

