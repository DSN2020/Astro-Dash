import pygame
from window import window_maker, width, height

player_color = "#ff00ff"
pos = (width // 2, height // 2)

class player_class:
    def player_draw(screen):
        pygame.draw.circle(screen, player_color, pos, 20)
    