# Pong game written in python using curses library
import curses

def create_window(nrows, ncols, posY, posX, title):
    win = curses.newwin(nrows,ncols,posY,posX)
    win.box('|','-')
    win.move(0,1)
    win.addstr(title)
    win.move(1,1)

    return win

def main(stdscr):
    
    win = create_window(20,20,10,10,'Window!')
    win.addstr("Hello World!")
    win.getch()

# Python permite inicializar automaticamente los recursos de ncurses
# gracias a la funcion wrapper.
if __name__ == '__main__':
    curses.wrapper(main)
