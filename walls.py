import player
from window import window_maker, width, height
screen = window_maker()

def restart():
    if player.x >= width -15 or player.x <= 15 or player.y >= height-15 or player.y <= 15:
        player.x = width // 2
        player.y = height // 2
        player.player_class.player_draw(screen)
