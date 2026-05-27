from window import window_maker
from player import player_class
import controls
import pygame
import walls

screen = window_maker()
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(90)
    controls.check_key_pressed()
    screen.fill(("#101046"))
    player_class.player_draw(screen)
    walls.restart()
    pygame.display.flip() #? updates diaplay

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Check for window close event
            running = False
    