from menus.mainMenu import MainMenu
from state import State

# class which instance everything of the game and main systems
class Game:

    # construct method
    def __init__(self):
        # main_menu | Stores MainMenu class
        self.main_menu = MainMenu()
        # state | Stores game state
        self.state = State.MAIN_MENU

    # updates everything of the game
    # @params screen : screen variable stored in main.py to get size of the window
    def update(self, screen):

        self.main_menu.update(screen)

    # updates everything of the game when video resize
    # @params screen : screen variable stored in main.py to get size of the window
    def update_video_resize(self, screen):

        self.main_menu.update_video_resize(screen)
