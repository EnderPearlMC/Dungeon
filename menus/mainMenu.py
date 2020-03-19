import pygame


# class which stores every part of the Main Menu and all systems of it
class MainMenu:

    # construct method
    def __init__(self):

        # font | Main font
        self.font = pygame.font.SysFont("Arial", 28)
        # font | Second font
        self.font2 = pygame.font.SysFont("Arial", 38, True)

        # add menu's elements
        self.add_elements()

    # add elements of the menu
    def add_elements(self):
        # background | Stores background image
        self.background = pygame.image.load("assets/images/mainMenu/background.png")
        # play_button | Stores play button image
        self.play_button = pygame.image.load("assets/images/mainMenu/playButton.png")
        # play_button_rect | Stores play button rect
        self.play_button_rect = self.play_button.get_rect()
        # coin_amount_text | Stores coin amount text
        self.coin_amount_text = self.font.render("", True, (255, 255, 255))
        # coin | Stores coin image
        self.coin = pygame.image.load("assets/images/mainMenu/coin.png")
        # buy_coins_text | Stores buy coins text
        self.buy_coins_text = self.font2.render("+", True, (255, 255, 255))
        # pseudo_text | Stores pseudo text
        self.pseudo_text = self.font.render("", True, (255, 255, 255))
        # level_text | Stores level text
        self.level_text = self.font2.render("", True, (225, 112, 85))
        # menu_button | Stores menu button image
        self.menu_button = pygame.image.load("assets/images/mainMenu/menuButton.png")
        # pseudo_text | Stores pseudo text
        self.loading_text = self.font.render("Loading...", True, (46, 204, 113))

    # @params screen : screen variable stored in main.py to get size of the window
    # @params game : screen variable stored in main.py to get game instance
    def update(self, screen, game):

        # render coin amount text
        self.coin_amount_text = self.font.render(str(game.game_data.data_player["money"]), True, (255, 255, 255))
        # render coin amount text
        self.buy_coins_text = self.font.render("+", True, (46, 204, 113))
        # render pseudo text
        self.pseudo_text = self.font.render(game.game_data.data_player["name"], True, (255, 255, 255))
        # render level text
        self.level_text = self.font2.render("Level " + str(game.game_data.data_player["level"]), True, (225, 112, 85))

        # reload background image
        self.background = pygame.image.load("assets/images/mainMenu/background.png")
        # set the size of it
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))

        # reload background image
        self.play_button = pygame.image.load("assets/images/mainMenu/playButton.png")
        # set the size of it
        self.play_button = pygame.transform.scale(self.play_button,
                                                  (int(screen.get_width() / 3.5), int(screen.get_height() / 5)))
        # get rect of play button
        self.play_button_rect = self.play_button.get_rect()
        # set pos
        self.play_button_rect.x = int(screen.get_width() / 2 - self.play_button.get_width() / 2)
        self.play_button_rect.y = int(screen.get_height() - screen.get_height() / 5)

        # reload background image
        self.coin = pygame.image.load("assets/images/mainMenu/coin.png")
        # set the size of it
        self.coin = pygame.transform.scale(self.coin, (50, 50))

        # reload menu button image
        self.menu_button = pygame.image.load("assets/images/mainMenu/menuButton.png")
        # set the size of it
        self.menu_button = pygame.transform.scale(self.menu_button, (40, 40))

        # render loading text
        self.loading_text = self.font.render("Loading...", True, (255, 255, 255))

    # detects if play button is clicked
    def is_play_button_pressed(self, pos):
        # if button clicked
        if self.play_button_rect.collidepoint(pos):
            return True
        else:
            return False
