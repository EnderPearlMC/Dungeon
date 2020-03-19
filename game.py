from levels.dungeons.Dungeon1Level import Dungeon1Level
from levels.secondMenuLevel import SecondMenuLevel
from menus.mainMenu import MainMenu
from state import State
from gameData import GameData
from entities.playerEntity import PlayerEntity
import os
import pygame


# class which instance everything of the game and main systems
class Game:

    # construct method
    # @params screen : screen variable stored in main.py
    def __init__(self, screen):
        # main_menu | Stores MainMenu class
        self.main_menu = MainMenu()
        # second_menu | Stores SecondMenuLevel class
        self.second_menu = SecondMenuLevel()
        # state | Stores game state
        self.state = State.MAIN_MENU
        # game_data | Stores GameData class
        self.game_data = GameData()
        # player | Stores the main player
        self.player = PlayerEntity(self)
        # key_pressed | Stores keys and if they are pressed
        self.keys_pressed = {}
        # current_dungeon | Stores the current dungeon
        self.current_dungeon = 0

        # ========================================
        #               DUNGEONS
        # ========================================
        # dungeon_1 | Stores Dungeon1Level class
        self.dungeon_1 = Dungeon1Level()
        # dungeons | Stores every dungeon
        self.dungeons = {
            1: self.dungeon_1
        }

    # updates everything of the game
    # @params screen : screen variable stored in main.py to get size of the window
    def update(self, screen):
        if self.state == State.MAIN_MENU:
            self.main_menu.update(screen, self)
        elif self.state == State.SECOND_MENU:
            if self.keys_pressed.get(97):
                self.player.move_left(self.second_menu)
            elif self.keys_pressed.get(100):
                self.player.move_right(self)
            elif self.keys_pressed.get(119):
                self.player.move_top(self.second_menu)
            elif self.keys_pressed.get(115):
                self.player.move_bottom(self.second_menu)

        if os.path.exists('files/player.yaml'):
            self.game_data.data_player = self.game_data.get_player_file_data()

        self.game_data.make_datas_as_file()

    # updates everything of the game when video resize
    # @params screen : screen variable stored in main.py to get size of the window
    # @param blocks_size : The size of the blocks
    def update_video_resize(self, screen, blocks_size):
        if self.state == State.SECOND_MENU:
            # update level
            self.second_menu.update(screen, (screen.get_width() / 2, screen.get_height() / 5), blocks_size)
            # resize player
            self.player.image = pygame.transform.scale(self.player.image, (blocks_size[0], blocks_size[1]))
        elif self.state == State.DUNGEON:
            self.dungeons.get(self.current_dungeon).update(screen, (screen.get_width() / 2, screen.get_height() / 5), blocks_size)

    # @param sprite1
    # @param sprites
    def check_collisions(self, sprite1, group2):
        return pygame.sprite.spritecollideany(sprite1, group2)