import pygame


# class which generates an isometric level
from blocks.Block import Block
from blocks.GrassBlock import GrassBlock


class IsometricLevel:

    # construct method
    # @param recoil : The recoil of the map
    def __init__(self):
        self.map = []
        self.blocks_group = pygame.sprite.Group()

    # generates the level
    # @params screen : screen variable stored in main.py to get size of the window
    # @param recoil : The recoil of the map
    # @param size : The size of the blocks
    def generate_level(self, screen, recoil, size):

        for idx, val in enumerate(self.map):
            for idx2, val2 in enumerate(val):
                for idx3, val3 in enumerate(val2):
                    x = ((idx - idx2) * size[0] / 2) + recoil[0]
                    y = (((idx + idx2) * size[1] / 4) - idx3 * (size[1] / 2)) + recoil[1]
                    if val3 != 0:
                        if val3 == Block.GRASS:
                            grass = GrassBlock()
                            grass.image = pygame.image.load("assets/images/blocks/isometric_0087.png")
                            grass.image = pygame.transform.scale(grass.image, (size[0], size[1]))
                            grass.rect.x = x
                            grass.rect.y = y
                            self.blocks_group.add(grass)
                            self.map[idx][idx2][idx3] = Block.GRASS_GENERATED

    # updates the level
    # @params screen : screen variable stored in main.py to get size of the window
    # @param recoil : The recoil of the map
    # @param size : The size of the blocks
    def update(self, screen, recoil, size):
        self.blocks_group.empty()
        for idx, val in enumerate(self.map):
            for idx2, val2 in enumerate(val):
                for idx3, val3 in enumerate(val2):
                    x = ((idx - idx2) * size[0] / 2) + recoil[0]
                    y = (((idx + idx2) * size[1] / 4) - idx3 * (size[1] / 2)) + recoil[1]
                    if val3 != 0:
                        if val3 == Block.GRASS_GENERATED:
                            grass = GrassBlock()
                            grass.image = pygame.image.load("assets/images/blocks/isometric_0087.png")
                            grass.image = pygame.transform.scale(grass.image, (size[0], size[1]))
                            grass.rect.x = x
                            grass.rect.y = y
                            self.blocks_group.add(grass)
