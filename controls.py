import pygame
import player
import window
import walls
#import Main #cant do this or is makes Main.py not be able to call on controls ? 

pygame.init()

vel = 20
screen = window.window_maker()

#new_pos = player.player
def move_up():
    player.y-= 15
    y_value = player.y
    
    print(f"{y_value}: x_value")
    print(player.pos)
    player.player_class.player_draw(screen)
    player.pos = (player.x, player.y) # draws new
    
    
def move_down():
    player.y+= 15
    y_value = player.y
    print(f"{y_value}: x_value")
    player.player_class.player_draw(screen)
    player.pos = (player.x, player.y)

def move_right():
    player.x+= 15
    x_value = player.y
    print(f"{x_value}: x_value")
    player.player_class.player_draw(screen)
    player.pos = (player.x, player.y)

def move_left():
    player.x-= 15
    x_value = player.x
    print(f"{x_value}: x_value")
    player.player_class.player_draw(screen)
    player.pos = (player.x, player.y)
    

def check_key_pressed():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move_up()
        print("keypressed")
    elif keys[pygame.K_DOWN]:
        move_down()
        print("keypressed")
    elif keys[pygame.K_LEFT]:
        move_left()
        print("keypressed")
    elif keys[pygame.K_RIGHT]:
        move_right()
        print("keypressed")



