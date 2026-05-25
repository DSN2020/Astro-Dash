import pygame
from window import window_maker, width, height

player_color = "#ff00ff"
start_pos= (width // 2, height // 2)

def player(screen):
    pygame.draw.circle(screen, player_color, start_pos, 20)