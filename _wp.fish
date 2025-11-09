#!/usr/bin/env fish

function set_wallpaper_image
    echo "$argv[1]"
    swww img --transition-type fade "$argv[1]"
end

function set_wallpaper_video
    mpvpaper -p -o 'no-audio' '*' "$argv[1]"
end

function set_wallpaper
    switch "$(path extension "$argv[1]" | string lower)"
    case .png .jp{,e}g
        set_wallpaper_image "$argv[1]"
    case .mp4 .mkv .webm .gif
        set_wallpaper_video "$argv[1]"
    case '*'
        echo "Error: unsupported file extension: $argv[1]"
        return 1
    end
end

function set_wallpaper_random
    set_wallpaper "$(random choice $argv)"
end

function print_help
    echo "\
Usage: $(status basename) [options] [files...]

Uses `swww` for image wallpapers and `mpvpaper` for video wallpapers.

- If no file is given, set the default wallpaper (environment:
  DEFAULT_WALLPAPER).
- If one file is given, set it as the wallpaper.
- If multiple files are given:
  - If -interval is given, run continously until CTRL-C, choosing a random file
    and setting it as the wallpaper at every interval.
  - Otherwise, choose a random file and set it as the wallpaper.

Options:
    -help
        Show this help message and exit.
    -interval [time]
        Random wallpaper interval when given multiple files.
        Supports time suffixes (see `man sleep`)."
end

function main
    argparse help interval= -- $argv
    or return

    if set -q _flag_help
        print_help
        return
    end

    switch "$(count $argv)"
    case 0
        set -q DEFAULT_WALLPAPER
        or set DEFAULT_WALLPAPER ~/media/wallpaper/default.jpg
        set_wallpaper "$DEFAULT_WALLPAPER"
    case 1
        set_wallpaper "$argv[1]"
    case '*'
        if set -q _flag_interval
            while true
                set_wallpaper_random $argv
                sleep "$_flag_interval"
            end
        else
            set_wallpaper_random $argv
        end
    end
end

main $argv
