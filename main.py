

import pygame

from game import Game
from state import State

# init pygame
pygame.init()

# create window
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
# set title of it
pygame.display.set_caption("Dungeon")

# ==========================================
#   VARIABLES
# ==========================================

# running | true : the window is running / false : the window doesn't run anymore
running = True
# game | Stores class Game
game = Game()


# draws everything of the game
def draw():

    # if game state is mainmenu
    if game.state == State.MAIN_MENU:
        # draw main menu
        screen.blit(game.main_menu.background, (0, 0))
        # draw play button
        screen.blit(game.main_menu.play_button, (int(screen.get_width() / 2 - game.main_menu.play_button.get_width() / 2), int(screen.get_height() - screen.get_height() / 5)))
        # draw coin amount text
        screen.blit(game.main_menu.coin_amount_text, (int(screen.get_width() - 120), 15))
        # draw coin
        screen.blit(game.main_menu.coin, (int((screen.get_width() - 120) - 60), 5))
        # draw buy coins text
        screen.blit(game.main_menu.buy_coins_text, (int((screen.get_width() - 120) + 76), 9))


# Main loop which updates all parts of the game
while running:


    # update window
    pygame.display.flip()
    # update everything of the game
    game.update(screen)

    # draw elements
    draw()

    # get events
    for e in pygame.event.get():

        # if cross is pressed
        if e.type == pygame.QUIT:
            # set running to False
            running = False
            # close window
            pygame.quit()


        # if window resizable
        if e.type == pygame.VIDEORESIZE:
            # recreate window with new dimensions
            screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            # update when video resize
            game.update_video_resize(screen)
