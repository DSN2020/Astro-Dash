import player
from window import window_maker, window_width, window_height
screen = window_maker()

def restart():
    if player.x >= window_width -15 or player.x <= 15 or player.y >= window_height-15 or player.y <= 15:
        player.x = window_width // 2
        player.y = window_height // 2
        player.player_class.player_draw(screen)
