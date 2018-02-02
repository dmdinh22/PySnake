# SNAKES GAME
# Arrow Keys to move snake
# Spacebar to start/stop gameplay
# Esc to exit

from random import randint
import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT 

# determines terminal type & initialize data structs
curses.initscr()
# create curses window
win = curses.newwin(20,60,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#initialize the values
score = 0
key = KEY_RIGHT #move right first 

#first food coord
food = [10,20] 
#initial snakes coords
snake=[[3,9], [3,8], [3,7]]
#print food
win.addch(food[0], food[1], '*')
#run until esc key pressed
while key != 27:
    win.border(0)
    # scoreboard
    win.addstr(0,2, ' Score: ' + str(score) + ' ')
    #snake title
    win.addstr(0,27, ' SNAKE ' )
    #increase speed as snake gets larger
    win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)

    #pressed previous key
    prevKey = key                                             
    event = win.getch()
    key = key if event == -1 else event

    # space bar presses to pause
    if key == ord(' '):
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue
    
    # if key pressed isn't one of the controls
    if key not in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, 27]:
        key = prevKey

    #calculate new coords of snake head 
    snake.insert(0, [snake[0][0] + (key == KEY_UP and -1) + (key == KEY_DOWN and 1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # make snake enter from other side when crossing boundary
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    # if snake runs over itself - GAME OVER
    if snake[0] in snake[1:]: break
    
    # when snake consumes the food
    if snake[0] == food:
        food =[]
        score += 1
        while food ==[]:
            #randomly place food again on screen
            food = [randint(1, 15), randint(1, 55)]
            if food in snake: food = []
        win.addch(food[0], food[1], '*')
    else: 
        #if it does not eat food, decrease length
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')

curses.endwin()
print("\nGAME OVER")
print("\nScore - " + str(score))