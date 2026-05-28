import pygame
from window import window_maker, window_width, window_height
import player
import random


class block:

    block_width_side = window_width / 20 # needs to be ranny long or wide
    block_height_side = window_height 
    block_width_top = window_width 
    block_height_top = window_height / 20

    

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw_left_block(self, screen):
        pygame.draw.rect(screen, "#ff005f", (13, 0, block.block_width_side, block.block_height_side))#! make a list for tuple locations
        print('left block')
    def draw_right_block(self, screen):
        pygame.draw.rect(screen, "#ff005f", (window_width - 13, 0, block.block_width_side, block.block_height_side))#! make a list for tuple locations
        print('right block')
    def draw_top_block(self, screen):
        pygame.draw.rect(screen, "#ff005f", (0, 13, block.block_width_top, block.block_height_top))#! make a list for tuple locations
        print('top_block')
    def draw_bottom_block(self, screen):
        pygame.draw.rect(screen, "#ff005f", (0, window_height- 13, block.block_width_top, block.block_height_top))#! make a list for tuple locations
        print('bottom block')
spawn_locations_x = [window_width-13, 0] # should make the bar spawn on the left or right side
spawn_locations_y = [window_height -13, -13]

active_targets = []
def spawn_targets():
    ranny_x = random.randint(0,1)#this will be used to pick inside the x list
    ranny_y = random.randint(0, 1)#this will be used to pick inside the y list
    
    if len(active_targets) < 1:
        killer_death_block = block(spawn_locations_x[ranny_x],spawn_locations_y[ranny_y])
        print(spawn_locations_x[ranny_x], spawn_locations_y[ranny_y])
        print(ranny_x, ranny_y)
        active_targets.append(killer_death_block)

ranny_x = random.randint(0,3)
def draw_targets(screen):
    if len(active_targets) > 0:
        for item in active_targets:
            print(active_targets)
            if ranny_x == 0:
                item.draw_top_block(screen)
            elif ranny_x == 1:
                item.draw_right_block(screen)
            elif ranny_x == 2:
                item.draw_bottom_block(screen)
            elif ranny_x == 3:
                item.draw_left_block(screen)
        