# Snake Game - desktop
import pygame
import sys
import random
import time
 
# check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    # no errors, go forth!
    print("(+) PyGame successfully initialized!")
 
# screen - set screen size
playCanvas = pygame.display.set_mode((720, 460))
pygame.display.set_caption('SNAKE')
 
red = pygame.Color(255, 0, 0) # gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food
 
# frame controller
frameController = pygame.time.Clock()
 
# variables
snkPosition = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]
 
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True
 
direction = 'RIGHT'
changedir = direction
 
score = 0
 
# game over method
def gameOver():
    def_font = pygame.font.SysFont('monaco', 72)
    GOsurf = def_font.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playCanvas.blit(GOsurf,GOrect)
    showScore(0)
    pygame.display.flip()
   
    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit() #console exit
   
# show score method
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score) , True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playCanvas.blit(Ssurf,Srect)
   
   
# game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changedir = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changedir = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changedir = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changedir = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
 
    # check direction
    if changedir == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changedir == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changedir == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changedir == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
 
    # move snake
    if direction == 'RIGHT':
        snkPosition[0] += 10
    if direction == 'LEFT':
        snkPosition[0] -= 10
    if direction == 'UP':
        snkPosition[1] -= 10
    if direction == 'DOWN':
        snkPosition[1] += 10
   
   
    # snake body
    snakeBody.insert(0, list(snkPosition))
    if snkPosition[0] == foodPos[0] and snkPosition[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
       
    # new food
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
   
    #background
    playCanvas.fill(white)
   
    #draw the snake
    for pos in snakeBody:
        pygame.draw.rect(playCanvas, green, pygame.Rect(pos[0],pos[1],10,10))
   
    pygame.draw.rect(playCanvas, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
   
    # bound
    if snkPosition[0] > 710 or snkPosition[0] < 0:
        gameOver()
    if snkPosition[1] > 450 or snkPosition[1] < 0:
        gameOver()
       
    # snake eat itself
    for block in snakeBody[1:]:
        if snkPosition[0] == block[0] and snkPosition[1] == block[1]:
            gameOver()
   
    showScore()
    pygame.display.flip()
   
    frameController.tick(24)