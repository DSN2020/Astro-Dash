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
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y) # draws new

def move_down():
    player.y+= 15
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y)

def move_right():
    player.x+= 15
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y)

def move_left():
    player.x-= 15
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y)
#diagnal moves
def move_up_left():
    player.x-= 15
    player.y-= 15
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y)
def move_up_right():
    player.x+= 15
    player.y-= 15
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y)
def move_bottom_left():
    player.x-= 15
    player.y+= 15
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y)
def move_bottom_right():
    player.x+= 15
    player.y+= 15
    print(f"{player.player_pos}: Player Position")
    player.player_class.player_draw(screen)
    player.player_pos = (player.x, player.y)
    

def check_key_pressed():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP8]:
        move_up()
        print("keypressed")
    elif keys[pygame.K_KP2]:
        move_down()
        print("keypressed")
    elif keys[pygame.K_KP4]:
        move_left()
        print("keypressed")
    elif keys[pygame.K_KP6]:
        move_right()
        print("keypressed")

        #diagnal
    elif keys[pygame.K_KP7]:
        move_up_left()
        print("topleft")
    elif keys[pygame.K_KP9]:
        move_up_right()
        print("topright")
    elif keys[pygame.K_KP1]:
        move_bottom_left()
        print("bottomleft")
    elif keys[pygame.K_KP3]:
        move_bottom_right()
        print("bottomright")
    
    
    



