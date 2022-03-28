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

def move_ball(win):
    maxX = curses.LINES
    #maxY = curses.COLS
    x = 1
    y = 1
    nextX = 0
    direction = 1

    curses.noecho()
    curses.curs_set(False)

    while True:
        win.clear()
        win.addch(y,x,'o')
        win.refresh()

        time.sleep(0.05)

        nextX = x + direction

        if (nextX >= maxX or nextX == 0):
            direction *= -1
        else:
            x += direction




def main(stdscr):
    
    win = create_window(curses.LINES,curses.COLS,10,10,'Pong')
    move_ball(win)
    #win.getch()

# Python permite inicializar automaticamente los recursos de ncurses
# gracias a la funcion wrapper.
if __name__ == '__main__':
    curses.wrapper(main)
