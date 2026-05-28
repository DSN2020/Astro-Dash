import pygame
import controls
from window import window_maker, window_width, window_height

player_color = "#ff00ff"
x = window_width //2 
y = window_height // 2
player_pos = (x, y)

class player_class:
    def player_draw(screen):
        pygame.draw.circle(screen, player_color, player_pos, 20)



    