"""Tic Tac Toe"""
# pylint: disable=no-member,unused-import,unused-variable,missing-function-docstring,redefined-outer-name,import-error
# Hides a ton of unnecessary pylint warnings

import time
import math
import os
import pygame
pygame.init()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Fix an error if the program is not executed from the program directory,
# by changing the working directory to the program directory

# User-adjustable variables
MAXFPS = 30  # Maximun FPS, to prevent too much CPU usage
theme = "dark"
# Dark vs light colors
Colorpallette = {
    "light": {
        "background": (245, 245, 245),
        "grid": (0, 0, 0),
        "symbol": (0, 0, 0)
    },
    "dark": {
        "background": (10, 10, 10),
        "grid": (255, 255, 255),
        "symbol": (200, 100, 200)
    }
}

# Internal variables
size = (600, 600)
lastTime = time.time()
RUNNING = True
state = (0, 0, 0,
         0, 0, 0,
         0, 0, 0)  # 0 -> empty; 1 -> X; -1 -> O

coordinates = ((160, 160), (300, 160), (440, 160),
               (160, 300), (300, 300), (440, 300),
               (160, 440), (300, 440), (440, 440))

window = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")
try:
    pygame.display.set_icon(pygame.image.load("Resources\\icon.png"))
except FileNotFoundError:
    pygame.display.set_icon(pygame.image.load("Resources/icon.png"))

# Functions

def drawcross(color, coords, h: float):
    pygame.draw.line(window, color, (coords[0] - h, coords[1] - h), (coords[0] + h, coords[0] + h), 4)
    pygame.draw.line(window, color, (coords[0] - h, coords[1] + h), (coords[1] + h, coords[1] - h), 4)

def gameloop(event):
    """Main game loop"""
    if event.type == 256:  # Close button pressed
        pygame.quit()
        exit(0)
    



def draw():
    # Draw the grid
    pygame.draw.line(window, Colorpallette[theme]["grid"], (220, 100), (220, 500), 4)
    pygame.draw.line(window, Colorpallette[theme]["grid"], (380, 100), (380, 500), 4)
    pygame.draw.line(window, Colorpallette[theme]["grid"], (100, 220), (500, 220), 4)
    pygame.draw.line(window, Colorpallette[theme]["grid"], (100, 380), (500, 380), 4)
    for i, j in enumerate(state):
        if j == 1:
            drawcross(Colorpallette[theme]["symbol"], coordinates[i], 40)
        elif j == -1:
            pygame.draw.circle(window, Colorpallette[theme]["symbol"], coordinates[i], 44, 4)
            # Extra 4 due to how thick circles are drawn in pygame

while RUNNING:
    # Code for measuring time
    Nowtime = time.time()
    dt = Nowtime - lastTime
    lastTime = Nowtime

    # Game code
    for e in pygame.event.get():
        gameloop(e)

    window.lock()
    window.fill(Colorpallette[theme]["background"])
    draw()
    window.unlock()
    pygame.display.update()

    # Code to limit FPS
    excess = 1/MAXFPS - dt
    if excess > 0:
        time.sleep(excess)


# Additional notes:
# Boxes are at:
# (160, 160), (300, 160), (440, 160),
# (160, 300), (300, 300), (440, 300),
# (160, 440), (300, 440), (440, 440)