import pygame
import player

pygame.init()

vel = 20


#new_pos = player.player
def move_up():
    player.player_class.player_draw().x +10
    
    
def move_down():
    new_pos -=20
    

def check_key_pressed():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move_up()
        print("keypressed")
    elif keys[pygame.K_DOWN]:
        move_down()
        print("keypressed")



