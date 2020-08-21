#########################################
# Programmer: Mrs G. & Mishelle Bitman
# Date: Nov,2019
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
#########################################
import pygame
pygame.init()
import time
from math import sqrt  # only sqrt function is needed from the math module
from random import randint

HEIGHT = 600
WIDTH = 800
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("happyBirth.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
end = pygame.image.load("gameOverScreen.png")
end = pygame.transform.scale(end, (800, 600))

start_time = time.time()

font = pygame.font.SysFont("Arial", 45)
WHITE = (255,255,255)
BLACK = (0, 0, 0)  # used colours
RED = (255, 0, 0)  ###
GREEN = (0, 255, 0)  ### define the main colours: R,G,B
BLUE = (0, 0, 255)
# Making random colors be chosen
# r=random(0,255)
# g=random(0,255)
# b=random(0,255)# used colours
outline = 0  # thickness of the shapes' outline
counter = 0
def gameOver():
    game_window.blit(end,(0,0))
    pygame.display.update()
########################################
# ---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
# ---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Pythagorean theorem
# ---------------------------------------#
# function that redraws all objects     #
# ---------------------------------------#
def redraw_game_window():
    game_window.blit(background, (0, 0))
    graphics = font.render("Score: " + str(counter), 1, BLACK)
    game_window.blit(graphics, (20, 50))
    pygame.display.update()

    for i in range(20):
        if balloonVisible[i] == True:
            pygame.draw.circle(game_window, balloonCLR[i], (balloonX[i], balloonY[i]), balloonR[i], outline)
            # display must be updated, in order
            # to show the drawings


    if balloonVisible == [False] * 20:         # To end the game:
        gameOver()
    pygame.display.update()


# ---------------------------------------#
# the main program begins here          #
# ---------------------------------------#
exit_flag = False  #
balloonR = [0] * 20  # create lists of 20 items each
balloonX = [0] * 20  # for balloons' properties
balloonY = [0] * 20  #
balloonSPEED = [0] * 20  #
balloonCLR = [0, 0, 0] * 20 #Random colour for each balloon
balloonVisible = [True] * 20
for i in range(20):
    balloonX[i] = randint(0, WIDTH)  # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT / 2, HEIGHT)
    balloonR[i] = randint(20, 50)
    balloonSPEED[i] = randint(3, 5)
    balloonCLR[i] = (randint(0, 255), randint(0, 255), randint(0, 255)) # Balloon in random colours
    balloonVisible[i] = True
while not exit_flag:  #
    for event in pygame.event.get():  # check for any events
        if event.type == pygame.QUIT:  # If user clicked close
            exit_flag = True  # Flag that we are done so we exit this loop
        # act upon mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(20):
                (cursorX, cursorY) = pygame.mouse.get_pos()
                if balloonVisible[i] == True:
                    if distance(cursorX, cursorY, balloonX[i], balloonY[i]) < balloonR[i]:
                        balloonVisible[i] = False
                        counter += 1
                        print("Balloons popped: ", counter)

    # move the balloons
    for i in range(20):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
        if balloonVisible[i] == True:
            if balloonY[i] + balloonR[i] < 0:
                balloonVisible[i] = False
    end_time = time.time()
    difference = int((end_time) - (start_time))
    print("The time elapsed is: ", difference, "seconds")
    redraw_game_window()

    
    pygame.time.delay(100)
    pygame.display.update()

pygame.quit()