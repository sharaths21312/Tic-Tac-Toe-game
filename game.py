"""Tic Tac Toe"""
# pylint: disable=no-member,unused-import,unused-variable,missing-function-docstring,redefined-outer-name,import-error
# Hides a ton of unnecessary pylint warnings

import os
import pygame
pygame.init()
font = pygame.font.SysFont("arial", 40)
textSurface = font.render("", True, (255, 255,255), (0, 0, 0))
textRect = pygame.Rect(1, 1, 1, 1)
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
        "symbol": (0, 0, 0),
        "Matchover": (200, 150, 150)
    },
    "dark": {
        "background": (10, 10, 10),
        "grid": (255, 255, 255),
        "symbol": (200, 100, 200),
        "Matchover": (70, 20, 20)
    }
}

# Internal variables
turn = 1 # 1 -> X, -1 -> O
clock = pygame.time.Clock()
size = (600, 600)
wins = [0, 0, 0] # Draws, X, O
RUNNING = True
state = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]  # 0 -> empty; 1 -> X; -1 -> O

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
    pygame.draw.line(window, color, (coords[0] - h, coords[1] - h), (coords[0] + h, coords[1] + h), 4)
    pygame.draw.line(window, color, (coords[0] - h, coords[1] + h), (coords[0] + h, coords[1] - h), 4)

def ResetBoard():
    global textSurface, textRect, state, turn
    stringval = "X: " + str(wins[1]) + " Draw: " + str(wins[0]) + " O: " + str(wins[2])
    state, turn = [0 for i in range(9)], 1
    textSurface = font.render(stringval, True, (255, 255,255))
    textRect = textSurface.get_rect()
    textRect.center = (300, 550)

def gameloop(event):
    global turn, state
    """Main game loop"""
    if event.type == 256:  # Close button pressed
        pygame.quit()
        exit(0)

    elif event.type == 1025: # Mouse Down
        if (0 not in state) or (abs(CheckWin()) == 1): ResetBoard(); return
        pos = pygame.mouse.get_pos()
        for i, j in enumerate(coordinates):
            if state[i] != 0: continue
            if ((j[0] - 70 < pos[0] < j[0] + 70) and (j[1] - 70 < pos[1] < j[1] + 70)):
                state[i] = turn
                turn = turn * -1
        if not CheckWin() == 0: wins[CheckWin()] += 1     



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
    
    

def CheckWin():
    for i in range(3):
        if state[3*i] == state[1 + 3*i] == state[2 + 3*i]: return state[1 + 3*i]
        if state[i] == state[i + 3] == state[i+6]: return state[i]
    if state[0] == state[4] == state[8]: return state[0]
    if state[2] == state[4] == state[6]: return state[3]
    return 0

ResetBoard()
while RUNNING:
    clock.tick(MAXFPS)

    # Game code
    for e in pygame.event.get():
        gameloop(e)

    window.lock()
    window.fill(Colorpallette[theme]["background"])
    if CheckWin(): window.fill(Colorpallette[theme]["Matchover"])
    draw()
    window.unlock()
    window.blit(textSurface, textRect)
    pygame.display.update()


# Additional notes:
# Boxes are at:
# (160, 160), (300, 160), (440, 160),
# (160, 300), (300, 300), (440, 300),
# (160, 440), (300, 440), (440, 440)