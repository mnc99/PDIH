# Pong game written in python using curses library
import curses
import time

def create_window(nrows, ncols, posY, posX, title):
    win = curses.newwin(nrows,ncols,posY,posX)
    win.box('|','-')
    win.move(0,1)
    win.addstr(title)
    win.move(1,1)

    return win

def move_ball(stdscr):
    maxY, maxX = stdscr.getmaxyx()
    posXBar1 = x = 1
    y = 1
    nextX = 0
    nextY = 0
    directionx = 1
    directiony = 1
    posYBar1 = int(round(maxY/2))

    curses.noecho()
    curses.curs_set(False)

    while (1):
        stdscr.clear()
        stdscr.addch(y,x,'o')
        stdscr.addstr(posYBar1, 0, '|')
        stdscr.addstr(posYBar1, maxX-1, '|')
        stdscr.refresh()

        time.sleep(0.05)

        nextX = x + directionx
        nextY = y + directiony

        if (nextX >= maxX or nextX < 0):
            directionx *= -1
        else:
            x += directionx

        if (nextY >= maxY or nextY < 0):
            directiony *= -1
        else:
            y += directiony




def main(stdscr):
    move_ball(stdscr)

# Python permite inicializar automaticamente los recursos de ncurses
# gracias a la funcion wrapper.
if __name__ == '__main__':
    curses.wrapper(main)
