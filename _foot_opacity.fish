#!/usr/bin/env fish

# NOTE: Change this to your terminal's background color. This is for gruvbox dark colorscheme.
set -q BG_COLOR
or set BG_COLOR "1d2021"

function print_help
    echo "Usage: $(status basename) [opacity from 0 to 100]"
end

function main
    argparse help -- $argv
    or return

    if set -q _flag_help
        print_help
        return
    end

    if set -q argv[1]
        if test "$argv[1]" -lt 0
            set argv[1] 0
        else if test "$argv[1]" -gt 100
            set argv[1] 100
        end

        printf '\033]11;[%s]#%s\033\\' "$argv[1]" "$BG_COLOR" >"$(tty)"
    else
        printf '\033]111\033\\' >"$(tty)"
    end
end

main $argv
