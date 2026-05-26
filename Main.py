from window import window_maker
from player import player
import controls
import pygame

screen = window_maker()
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    controls.check_key_pressed()
    player(screen)
    pygame.display.flip() #? updates diaplay

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Check for window close event
            running = False
    