import pygame

from blocks.brickBlock import BrickBlock


# class which stores the main player
from blocks.grassBlock import GrassBlock


class PlayerEntity(pygame.sprite.Sprite):

    # construct method
    # @param game : instance of the class Game
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("assets/images/entities/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.velocity_x = 8
        self.velocity_y = 8

        self.game = game

    def move_right(self, game):
        if self.game.check_collisions(self, self.game.second_menu.blocks_group) != BrickBlock():
            self.rect.x += self.velocity_x

    def move_left(self, second_menu):
        self.rect.x -= self.velocity_x

    def move_top(self, second_menu):
        self.rect.y -= self.velocity_y

    def move_bottom(self, second_menu):
        self.rect.y += self.velocity_y
