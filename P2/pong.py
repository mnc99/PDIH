# Pong game written in python using curses library
import curses
import time
from random import randint

def create_window(rows, cols, posY, posX, title):
    win = curses.newwin(rows,cols,posY,posX)
    win.box()
    win.move(0,1)
    win.addstr(title)
    win.move(1,1)

    return win

def create_centered_window(rows, cols, title):
    y = (curses.LINES - rows) // 2
    x = (curses.COLS - cols) // 2

    return create_window(rows, cols, y, x, title)

def get_player_name(win,msg):
    curses.echo()
    win.addstr(msg)
    win.move(3,1)
    name = win.getstr()

    return name

def welcome_window(stdscr,playersNames):
    rows, cols = stdscr.getmaxyx()
    curses.curs_set(0)
    welcome = create_centered_window(rows, cols, "Welcome to Pong!")
    welcome.addstr(rows // 3, 10, playersNames[0] + " controls:")
    welcome.addstr((rows // 3)+2, 10, "Up --> Press 'a'")
    welcome.addstr((rows // 3)+4, 10, "Down --> Press 'z'")
    welcome.addstr(rows // 3, cols-len("Up --> Press 'k'")-10, playersNames[1] + " controls:")
    welcome.addstr((rows // 3)+2, cols-len("Up --> Press 'k'")-10, "Up --> Press 'k'")
    welcome.addstr((rows // 3)+4, cols-len("Up --> Press 'k'")-10, "Down --> Press 'm'")
    welcome.getch()

def game_over_window(stdscr, player):
    rows, cols = stdscr.getmaxyx()
    curses.curs_set(0)
    game_over = create_centered_window(rows, cols, "Game Over!")
    xmsg = int((cols // 2) - (len(player) // 2) - len(player) % 2)
    ymsg = int((rows // 2) - 2)
    game_over.addstr(ymsg, xmsg, player + " wins!")
    game_over.getch()

def move_ball(stdscr, playersNames):
    maxY, maxX = stdscr.getmaxyx()
    ballPosition = [maxX // 2, maxY // 2]
    nextX = 0
    nextY = 0
    directions = (1,-1)
    directionx = directions[randint(0,1)]
    directiony = 1
    bar1Pos = [2, maxY // 2]
    bar2Pos = [maxX-3, maxY // 2]
    k = 0
    halfX = maxX // 2
    pointsPl1 = pointsPl2 = 0
    gameOver = False

    curses.noecho()
    curses.curs_set(0)
    stdscr.nodelay(1)

    while (k != ord('q') and gameOver == False):
        stdscr.clear()

        # Divide screen in half
        for i in range(maxY):
            stdscr.addstr(i,halfX, '|')

        for i in range(maxX):
            stdscr.addstr(2,i,'-')

        for i in range(maxX):
            stdscr.addstr(maxY-2,i,'-')

        # Ball
        stdscr.addch(ballPosition[1],ballPosition[0],'o')

        # Left bar
        stdscr.addstr(bar1Pos[1]-2, 2, '|')
        stdscr.addstr(bar1Pos[1]-1, 2, '|')
        stdscr.addstr(bar1Pos[1], 2, '|')
        stdscr.addstr(bar1Pos[1]+1, 2, '|')
        stdscr.addstr(bar1Pos[1]+2, 2, '|')

        # Rigth bar
        stdscr.addstr(bar2Pos[1]-2, maxX-3, '|')
        stdscr.addstr(bar2Pos[1]-1, maxX-3, '|')
        stdscr.addstr(bar2Pos[1], maxX-3, '|')
        stdscr.addstr(bar2Pos[1]+1, maxX-3, '|')
        stdscr.addstr(bar2Pos[1]+2, maxX-3, '|')

        # Points
        stdscr.addstr(1, halfX-3, str(pointsPl1))
        stdscr.addstr(1, halfX+3, str(pointsPl2))

        # Info
        stdscr.addstr(1, 1, playersNames[0])
        stdscr.addstr(1, maxX-len(playersNames[1])-1, playersNames[1])
        stdscr.addstr(maxY-1, 1, "Press 'q' to exit")
        stdscr.refresh()

        time.sleep(0.04)

        nextX = ballPosition[0] + directionx
        nextY = ballPosition[1] + directiony

        if (nextX >= maxX or nextX < 0):
            directionx *= -1
        else:
            ballPosition[0] += directionx

        if (nextY >= maxY-1 or nextY < 2):
            directiony *= -1
        else:
            ballPosition[1] += directiony

        k = stdscr.getch()

        #Controls for left bar
        if (k == ord('a')):
            bar1Pos[1] -= 2
        elif (k == ord('z')):
            bar1Pos[1] += 2

        #Controls for right bar
        if (k == ord('k')):
            bar2Pos[1] -= 2
        elif (k == ord('m')):
            bar2Pos[1] += 2

        # Check new positions of bars
        bar1Pos[1] = max(5, bar1Pos[1])
        bar1Pos[1] = min(maxY-5, bar1Pos[1])
        bar2Pos[1] = max(5, bar2Pos[1])
        bar2Pos[1] = min(maxY-5, bar2Pos[1])

        if (ballPosition[0] == 0):
            pointsPl2 += 1
            ballPosition[0] = maxX // 2
            ballPosition[1] = randint(2, maxY-1)
            directionx = 1

        if (ballPosition[0] == maxX-1):
            pointsPl1 += 1
            ballPosition[0] = maxX // 2
            ballPosition[1] = randint(2, maxY-1)
            directionx = -1

        # Making the ball bounce in left bar
        if (ballPosition[0] == bar1Pos[0] and ballPosition[1] == bar1Pos[1]+2):
            directionx *= 1
            directiony *= -1
        elif (ballPosition[0] == bar1Pos[0] and ballPosition[1] == bar1Pos[1]+1):
            directionx *= 1
            directiony *= -1
        elif (ballPosition[0] == bar1Pos[0] and ballPosition[1] == bar1Pos[1]):
            directionx *= -1
            directiony *= -1
        elif (ballPosition[0] == bar1Pos[0] and ballPosition[1] == bar1Pos[1]-1):
            directionx *= -1
            directiony *= -1
        elif (ballPosition[0] == bar1Pos[0] and ballPosition[1] == bar1Pos[1]-2):
            directionx *= -1
            directiony *= -1

        # Making the ball bounce in right bar
        if (ballPosition[0] == bar2Pos[0] and ballPosition[1] == bar2Pos[1]+2):
            directionx *= -1
            directiony *= 1
        elif (ballPosition[0] == bar2Pos[0] and ballPosition[1] == bar2Pos[1]+1):
            directionx *= -1
            directiony *= 1
        elif (ballPosition[0] == bar2Pos[0] and ballPosition[1] == bar2Pos[1]):
            directionx *= -1
            directiony *= -1
        elif (ballPosition[0] == bar2Pos[0] and ballPosition[1] == bar2Pos[1]-1):
            directionx *= -1
            directiony *= -1
        elif (ballPosition[0] == bar2Pos[0] and ballPosition[1] == bar2Pos[1]-2):
            directionx *= -1
            directiony *= -1

        # Game over
        if (pointsPl1 == 10):
            game_over_window(stdscr, playersNames[0])
            gameOver = True
        elif (pointsPl2 == 10):
            game_over_window(stdscr, playersNames[1])
            gameOver = True




def main(stdscr):
    # Get names of the two players
    win = create_centered_window(5, 40, "Welcome to Pong!")
    player1 = get_player_name(win, "Enter player 1 name:")
    win.erase()

    win = create_centered_window(5, 40, "Welcome to Pong!")
    player2 = get_player_name(win, "Enter player 2 name:")
    win.erase()

    playersNames = (player1, player2)

    # Launch welcome window
    welcome_window(stdscr, playersNames)

    # Start game
    move_ball(stdscr, playersNames)

# Python permite inicializar y liberar automaticamente los recursos de curses
# gracias a la funcion wrapper.
if __name__ == '__main__':
    curses.wrapper(main)
