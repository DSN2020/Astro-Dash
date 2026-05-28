import pygame
from window import window_maker, window_width, window_height
import player
import random


class block:

    block_width = window_width / 20
    block_height = window_height / 20
    

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw_block(self, screen):
        pygame.draw.rect(screen, "#ff005f", (self.x, self.y, block.block_width, block.block_height))#! make a list for tuple locations

    
active_targets = []
def spawn_targets():
    ranny = random.randint(0,window_width)
    ranny2 = random.randint(0, window_height)
    
    if len(active_targets) < 7:
        killer_death_block = block(ranny,ranny2)
        print(ranny, ranny2)
        active_targets.append(killer_death_block)
    
def draw_targets(screen):
    if len(active_targets) > 0:
        for item in active_targets:
            item.draw_block(screen)
        