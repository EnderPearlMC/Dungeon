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
        # coin_amount_text | Stores coin amount text
        self.coin_amount_text = self.font.render("1500", True, (255, 255, 255))
        # coin | Stores coin image
        self.coin = pygame.image.load("assets/images/mainMenu/coin.png")
        # buy_coins_text | Stores buy coins text
        self.buy_coins_text = self.font2.render("+", True, (255, 255, 255))

    # @params screen : screen variable stored in main.py to get size of the window
    def update(self, screen):

        # render coin amount text
        self.coin_amount_text = self.font.render("1500", True, (255, 255, 255))
        # render coin amount text
        self.buy_coins_text = self.font2.render("+", True, (46, 204, 113))

    # @params screen : screen variable stored in main.py to get size of the window
    def update_video_resize(self, screen):
        # reload background image
        self.background = pygame.image.load("assets/images/mainMenu/background.png")
        # set the size of it
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))

        # reload background image
        self.play_button = pygame.image.load("assets/images/mainMenu/playButton.png")
        # set the size of it
        self.play_button = pygame.transform.scale(self.play_button, (int(screen.get_width() / 3.5), int(screen.get_height() / 5)))

        # reload background image
        self.coin = pygame.image.load("assets/images/mainMenu/coin.png")
        # set the size of it
        self.coin = pygame.transform.scale(self.coin, (50, 50))
