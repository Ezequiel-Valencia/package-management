#!/bin/sh
case "$1" in
  status)
    t=$(hyprctl hyprsunset temperature 2>/dev/null)
    echo "$t"
    if [ -n "$t" ] && [ "$t" -lt 6000 ]; 
      then echo true; 
      else echo false; 
    fi
    ;;
  *)
    if [ "$SWAYNC_TOGGLE_STATE" = true ]; then
      hyprctl hyprsunset temperature 3000
    else
      hyprctl hyprsunset identity
    fi
    ;;
esac