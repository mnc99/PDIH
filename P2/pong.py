# Pong game written in python using curses library
import curses
import time

def create_window(rows, cols, posY, posX, title):
    win = curses.newwin(rows,cols,posY,posX)
    win.box('|','-')
    win.move(0,1)
    win.addstr(title)
    win.move(1,1)

    return win

def create_centered_window(rows, cols, title):
    y = (curses.LINES - rows) // 2
    x = (curses.COLS - cols) // 2

    return create_window(rows, cols, y, x, title)


def welcome_window():
    rows = 25
    cols = 80
    curses.curs_set(0)
    welcome = create_centered_window(rows, cols, "Welcome to Pong!")
    welcome.addstr(rows // 4, 2, "Player 1 controls:")
    welcome.addstr((rows // 4)+2, 2, "Up --> Press 'a'")
    welcome.addstr((rows // 4)+4, 2, "Down --> Press 'z'")
    welcome.addstr(rows // 4, cols-len("Player 2 controls:")-3, "Player 2 controls:")
    welcome.addstr((rows // 4)+2, cols-len("Up --> Press 'k'")-5, "Up --> Press 'k'")
    welcome.addstr((rows // 4)+4, cols-len("Up --> Press 'k'")-5, "Down --> Press 'm'")
    welcome.getch()

def move_ball(stdscr):
    maxY, maxX = stdscr.getmaxyx()
    posXBar1 = xBall = 1
    yBall = 1
    nextX = 0
    nextY = 0
    directionx = 1
    directiony = 1
    posYBar1 = posYBar2 = maxY // 2
    upperYBar1 = 0
    upperYBar2 = 0
    k = 0
    halfX = maxX // 2
    pointsPl1 = pointsPl2 = 0

    curses.noecho()
    curses.curs_set(0)
    stdscr.nodelay(1)

    while (k != ord('q')):
        stdscr.clear()

        # Dividir la pantalla por la mitad
        for i in range(maxY):
            stdscr.addstr(i,halfX, '|')

        for i in range(maxX):
            stdscr.addstr(2,i,'-')

        for i in range(maxX):
            stdscr.addstr(maxY-2,i,'-')

        stdscr.addch(yBall,xBall,'o')
        stdscr.addstr(posYBar1-2, 0, '|')
        stdscr.addstr(posYBar1-1, 0, '|')
        stdscr.addstr(posYBar1, 0, '|')
        stdscr.addstr(posYBar1+1, 0, '|')
        stdscr.addstr(posYBar1+2, 0, '|')
        stdscr.addstr(posYBar2-2, maxX-1, '|')
        stdscr.addstr(posYBar2-1, maxX-1, '|')
        stdscr.addstr(posYBar2, maxX-1, '|')
        stdscr.addstr(posYBar2+1, maxX-1, '|')
        stdscr.addstr(posYBar2+2, maxX-1, '|')
        stdscr.addstr(1, halfX-3, str(pointsPl1))
        stdscr.addstr(1, halfX+3, str(pointsPl2))
        stdscr.addstr(1, 1, "Player 1")
        stdscr.addstr(1, maxX-len("Player 2")-1, "Player 2")
        stdscr.addstr(maxY-1, 1, "Press 'q' to exit")
        stdscr.refresh()

        time.sleep(0.05)

        nextX = xBall + directionx
        nextY = yBall + directiony
        upperYBar1 = posYBar1-2
        upperYBar2 = posYBar2-2

        if (nextX >= maxX or nextX < 0):
            directionx *= -1
        else:
            xBall += directionx

        if (nextY >= maxY-1 or nextY < 2):
            directiony *= -1
        else:
            yBall += directiony

        k = stdscr.getch()

        #Controls for left bar
        if (k == ord('a')):
            posYBar1 -= 1 if (upperYBar1-1) > 0 else posYBar1
        elif (k == ord('z')):
            posYBar1 += 1 if (posYBar1+1) < maxY else posYBar1

        #Controls for right bar
        if (k == ord('k')):
            posYBar2 -= 1 if (upperYBar2-1) > 0 else posYBar2
        elif (k == ord('m')):
            posYBar2 += 1 if (posYBar2+1) < maxY else posYBar2


def main(stdscr):
    welcome_window()
    move_ball(stdscr)

# Python permite inicializar y liberar automaticamente los recursos de curses
# gracias a la funcion wrapper.
if __name__ == '__main__':
    curses.wrapper(main)
