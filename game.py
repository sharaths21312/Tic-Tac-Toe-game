"""Tic Tac Toe"""
# pylint: disable=no-member,unused-import
import time
import math
import pygame

pygame.init()
size = (900, 600)
MAXFPS = 30

window = pygame.display.set_mode(size)

pygame.display.set_caption("A simple game")
pygame.display.set_icon(pygame.image.load("Resources/icon.png"))

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
