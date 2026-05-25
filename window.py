import pygame

width = 800
height = 800

def window_maker():
    pygame.init()
    
    screen = pygame.display.set_mode((width,height))
    screen.fill("#101046")

    pygame.display.set_caption("Astro Dash")

    running = True
    return screen

# Quit Pygame
pygame.quit()
