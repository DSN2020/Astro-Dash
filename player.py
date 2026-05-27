import pygame
import controls
from window import window_maker, width, height

player_color = "#ff00ff"
x = width //2 
y = height // 2
pos = (x, y)

class player_class:
    def player_draw(screen):
        pygame.draw.circle(screen, player_color, pos, 20)
        
    