"""Tic Tac Toe"""
# pylint: disable=no-member,unused-import
import time
import math
import os
import pygame

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Fix an error if the program is not executed from the program directory,
# by changing the working directory to the program directory

pygame.init()
size = (900, 600) # Size of display
MAXFPS = 30 # Maximun FPS, to prevent too much CPU usage

window = pygame.display.set_mode(size)

pygame.display.set_caption("Tic Tac Toe")
try:
    pygame.display.set_icon(pygame.image.load("Resources\\icon.png"))
except FileNotFoundError:
    pygame.display.set_icon(pygame.image.load("Resources/icon.png"))
# Linux vs windows

RUNNING = True
lastTime = time.time()
while RUNNING:
    # Code for measuring time
    Nowtime = time.time()
    dt = Nowtime - lastTime
    lastTime = Nowtime

    # Game code
    window.fill((200, 100, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    pygame.display.update()

    # Code to limit FPS
    excess = 1/MAXFPS - dt

    if excess > 0:
        time.sleep(excess)
