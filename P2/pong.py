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
    posXBar1 = xBall = 1
    yBall = 1
    nextX = 0
    nextY = 0
    directionx = 1
    directiony = 1
    posYBar1 = posYBar2 = int(round(maxY/2))
    k = 0
    halfX = int(round(maxX/2))
    pointsPl1 = pointsPl2 = 0

    curses.noecho()
    curses.curs_set(0)
    stdscr.nodelay(1)

    while (k != ord('q')):
        stdscr.clear()

        # Dividir la pantalla por la mitad
        for i in range(maxY):
            stdscr.addstr(i,halfX, '|')

        stdscr.addch(yBall,xBall,'o')
        stdscr.addstr(posYBar1, 0, '|')
        stdscr.addstr(posYBar2, maxX-1, '|')
        stdscr.addstr(1, halfX-3, str(pointsPl1))
        stdscr.addstr(1, halfX+3, str(pointsPl2))
        stdscr.refresh()

        time.sleep(0.05)

        nextX = xBall + directionx
        nextY = yBall + directiony

        if (nextX >= maxX or nextX < 0):
            directionx *= -1
        else:
            xBall += directionx

        if (nextY >= maxY or nextY < 0):
            directiony *= -1
        else:
            yBall += directiony

        k = stdscr.getch()

        #Controls for left bar
        if (k == ord('a')):
            posYBar1 -= 1 if (posYBar1-1) > 0 else posYBar1
        elif (k == ord('z')):
            posYBar1 += 1 if (posYBar1+1) < maxY else posYBar1

        #Controls for right bar
        if (k == ord('k')):
            posYBar2 -= 1 if (posYBar2-1) > 0 else posYBar2
        elif (k == ord('m')):
            posYBar2 += 1 if (posYBar2+1) < maxY else posYBar2


def main(stdscr):
    move_ball(stdscr)

# Python permite inicializar automaticamente los recursos de ncurses
# gracias a la funcion wrapper.
if __name__ == '__main__':
    curses.wrapper(main)
