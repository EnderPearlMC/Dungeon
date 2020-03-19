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
# blocks_size | Stores the size of the blocks that will be generated
blocks_size = (100, 116)


# draws everything of the game
def draw():
    # if game state is mainmenu
    if game.state == State.MAIN_MENU:
        # draw main menu
        screen.blit(game.main_menu.background, (0, 0))
        # draw play button
        screen.blit(game.main_menu.play_button, game.main_menu.play_button_rect)
        # draw coin amount text
        screen.blit(game.main_menu.coin_amount_text,
                    (int(screen.get_width() - game.main_menu.coin_amount_text.get_width() - 60), 15))
        # draw coin image
        screen.blit(game.main_menu.coin,
                    (int((screen.get_width() - 120) - game.main_menu.coin_amount_text.get_width()), 5))
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
        screen.fill((0, 206, 201))
        # draw block group
        game.second_menu.blocks_group.draw(screen)
        # draw the player
        screen.blit(game.player.image, game.player.rect)
    elif game.state == State.DUNGEON:
        screen.fill((0, 206, 201))
        # draw block group
        game.dungeons.get(game.current_dungeon).blocks_collision_group.draw(screen)
        game.dungeons.get(game.current_dungeon).blocks_group.draw(screen)
        # draw the player
        screen.blit(game.player.image, game.player.rect)


# works when mouse click is up
def mouse_button_up():
    if game.state == State.MAIN_MENU:
        if game.main_menu.is_play_button_pressed(pygame.mouse.get_pos()):
            game.state = State.DUNGEON
            game.current_dungeon = game.game_data.data_player['dungeon']
            # generate dungeon 1 level
            game.dungeons.get(game.current_dungeon).generate_level(screen, (screen.get_width() / 2, screen.get_height() / 5), blocks_size)
            # resize player
            game.player.image = pygame.transform.scale(game.player.image, (blocks_size[0], blocks_size[1]))


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
            running = True
            # close window
            pygame.quit()

        # if mouse up
        if e.type == pygame.MOUSEBUTTONUP:
            mouse_button_up()

        # if key down
        if e.type == pygame.KEYDOWN:
            # set the key as True in the key pressed dictionary
            game.keys_pressed[e.key] = True

        # if key up
        if e.type == pygame.KEYUP:
            # set the key as False in the key pressed dictionary
            game.keys_pressed[e.key] = False

        # if window resizable
        if e.type == pygame.VIDEORESIZE:

            # recreate window with new dimensions
            screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            # assign new size for the size of the blocks
            if screen.get_width() < 1280 and screen.get_width() > 800:
                blocks_size = (80, 96)
            elif screen.get_width() < 800:
                blocks_size = (60, 76)
            else:
                blocks_size = (100, 116)
            if screen.get_height() < 720 and screen.get_height() > 600:
                blocks_size = (80, 96)
            elif screen.get_height() < 600:
                blocks_size = (60, 76)
            else:
                blocks_size = (100, 116)

            # update
            game.update_video_resize(screen, blocks_size)
