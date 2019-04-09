import time
import sys
import curses

def testGUI(stdscr):

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)

    color = 1

    for i in range(100):
        while True:
            stdscr.erase()
            stdscr.addstr(0,10,"more sensors",curses.color_pair(color))
            stdscr.refresh()
            color += 1
            if color == 3:
                color = 1

            time.sleep(0.1)

curses.wrapper(testGUI)
