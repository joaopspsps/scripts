#!/usr/bin/env python
"""Play the "The Matrix has you..." animation on your terminal.

Reworked from <https://github.com/narkhy/MatrixHasYou> to use `curses`
instead of `print` and `system("clear")`. The timings are supposedly faithful
to the movie scene.

For better immersion, launch a terminal with a bigger font size and a retro
font (e.g., Fixedsys).
"""

import argparse
import curses
import locale
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "name",
        type=str,
        nargs="?",
        default="Neo",
        help="Name to show in the animation (default: %(default)s)",
    )
    args = parser.parse_args()

    msg1_text = f"Wake up, {args.name}..."
    msg2_text = "The Matrix has you..."
    msg3_text = "Follow the white rabbit."
    msg4_text = f"Knock, knock, {args.name}."

    msg1_wait = (
        [0.15, 0.1625, 0.15, 0.1625, 0.15, 0.1625, 0.15, 0.12]
        + [0.125] * len(args.name)
        + [0.0625, 0.0875, 0.0625, 0]
    )
    msg2_wait = [
        0.7325,
        0.67,
        0.6,
        0.78,
        0.095,
        0.135,
        0.1075,
        0.5275,
        0.6225,
        0.008,
        0.12,
        0.1475,
        0.45,
        0.008,
        0.4275,
        0.1275,
        0.1425,
        0.355,
        0.2275,
        0.145,
        0,
    ]
    msg3_wait = 0.1167

    msg1_wait_end = 16.03
    msg2_wait_end = 7.54
    msg3_wait_end = 8.515
    msg4_wait_end = 4

    locale.setlocale(locale.LC_ALL, "")

    scr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)

    curses.init_color(1, 0, 1000, 0)  # True green (RGB #0f0)
    curses.init_color(2, 0, 0, 0)  # True black (RGB #000)
    curses.init_pair(1, 1, 2)

    scr.bkgdset(" ", curses.color_pair(1))
    scr.clear()
    scr.refresh()

    win = curses.newwin(1, curses.COLS // 3, curses.LINES // 5, curses.COLS // 8)
    win.bkgdset(" ", curses.color_pair(1) | curses.A_BOLD)
    win.clear()
    win.refresh()

    try:
        while True:
            win.clear()
            for ch, sec in zip(msg1_text, msg1_wait):
                win.addstr(ch)
                win.refresh()
                time.sleep(sec)
            time.sleep(msg1_wait_end)

            win.clear()
            for ch, sec in zip(msg2_text, msg2_wait):
                win.addstr(ch)
                win.refresh()
                time.sleep(sec)
            time.sleep(msg2_wait_end)

            win.clear()
            for ch in msg3_text:
                win.addstr(ch)
                win.refresh()
                time.sleep(msg3_wait)
            time.sleep(msg3_wait_end)

            win.clear()
            win.addstr(msg4_text)
            win.refresh()
            time.sleep(msg4_wait_end)
    except KeyboardInterrupt:
        curses.endwin()


if __name__ == "__main__":
    main()
