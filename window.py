import pygame

window_width = 800
window_height = 800

def window_maker():
    pygame.init()
    
    screen = pygame.display.set_mode((window_width,window_height))
    screen.fill("#101046")

    pygame.display.set_caption("Astro Dash")

    running = True
    return screen

# Quit Pygame
pygame.quit()
