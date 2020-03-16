from levels.secondMenuLevel import SecondMenuLevel
from menus.mainMenu import MainMenu
from state import State
from gameData import GameData
import os


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

    # updates everything of the game
    # @params screen : screen variable stored in main.py to get size of the window
    def update(self, screen):
        if self.state == State.MAIN_MENU:
            self.main_menu.update(screen, self)

        if os.path.exists('files/player.yaml'):
            self.game_data.data_player = self.game_data.get_player_file_data()

        self.game_data.make_datas_as_file()

    # updates everything of the game when video resize
    # @params screen : screen variable stored in main.py to get size of the window
    def update_video_resize(self, screen):
        if self.state == State.SECOND_MENU:
            # update level
            self.second_menu.update(screen, (screen.get_width() / 2, screen.get_height() / 5), (100, 116))
