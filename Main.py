from window import window_maker
from player import player
import pygame

screen = window_maker()

running = True
while running:
    player(screen)
    pygame.display.flip() #? updates diaplay

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Check for window close event
            running = False
    