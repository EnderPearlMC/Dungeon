from menus.mainMenu import MainMenu
from state import State
from gameData import GameData

# class which instance everything of the game and main systems
class Game:

    # construct method
    def __init__(self):
        # main_menu | Stores MainMenu class
        self.main_menu = MainMenu()
        # state | Stores game state
        self.state = State.MAIN_MENU
        # game_data | Stores GameData class
        self.game_data = GameData()

    # updates everything of the game
    # @params screen : screen variable stored in main.py to get size of the window
    def update(self, screen):

        self.main_menu.update(screen)

        self.game_data.data_player = self.game_data.get_player_file_data()
        self.game_data.make_datas_as_file()

    # updates everything of the game when video resize
    # @params screen : screen variable stored in main.py to get size of the window
    def update_video_resize(self, screen):

        self.main_menu.update_video_resize(screen)
