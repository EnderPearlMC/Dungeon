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
game = Game(screen)


# draws everything of the game
def draw():
    # if game state is mainmenu
    if game.state == State.MAIN_MENU:
        # draw main menu
        screen.blit(game.main_menu.background, (0, 0))
        # draw play button
        screen.blit(game.main_menu.play_button, game.main_menu.play_button_rect)
        # draw coin amount text
        screen.blit(game.main_menu.coin_amount_text, (int(screen.get_width() - game.main_menu.coin_amount_text.get_width() - 60), 15))
        # draw coin image
        screen.blit(game.main_menu.coin, (int((screen.get_width() - 120) - game.main_menu.coin_amount_text.get_width()), 5))
        # draw buy coins text
        screen.blit(game.main_menu.buy_coins_text, (int((screen.get_width() - 120) + 76), 15))
        # draw pseudo text
        screen.blit(game.main_menu.pseudo_text, (10, screen.get_height() - game.main_menu.pseudo_text.get_height() - 5))
        # draw level text
        screen.blit(game.main_menu.level_text, (70, 10))
        # draw menu button image
        screen.blit(game.main_menu.menu_button, (10, 10))
    # if game state is second menu
    elif game.state == State.SECOND_MENU:
        # draw block group
        game.second_menu.blocks_group.draw(screen)


# works when mouse click is up
def mouse_button_up():
    if game.state == State.MAIN_MENU:
        if game.main_menu.is_play_button_pressed(pygame.mouse.get_pos()):
            screen.fill((0, 0, 0, 0))
            game.state = State.SECOND_MENU
            # generate second menu level
            game.second_menu.generate_level(screen, (screen.get_width() / 2, screen.get_height() / 5), (100, 116))


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

        # if mouse up
        if e.type == pygame.MOUSEBUTTONUP:
            mouse_button_up()

        # if window resizable
        if e.type == pygame.VIDEORESIZE:
            # recreate window with new dimensions
            screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            # update
            game.update_video_resize(screen)
