import pygame

from blocks.block import Block
from blocks.grassBlock import GrassBlock
from blocks.brickBlock import BrickBlock
from blocks.stoneBrickBlock import StoneBrickBlock
from blocks.magmaBlock import MagmaBlock


# class which generates an isometric level
class IsometricLevel:

    # construct method
    # @param recoil : The recoil of the map
    def __init__(self):
        self.map = []
        self.collision_map = []
        self.blocks_group = pygame.sprite.Group()
        self.blocks_collision_group = pygame.sprite.Group()

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
                    self.choose_block_when_generation(idx, idx2, idx3, size, x, y, val3, "bg")

        for idx, val in enumerate(self.collision_map):
            for idx2, val2 in enumerate(val):
                for idx3, val3 in enumerate(val2):
                    x = ((idx - idx2) * size[0] / 2) + recoil[0]
                    y = (((idx + idx2) * size[1] / 4) - idx3 * (size[1] / 2)) + recoil[1]
                    self.choose_block_when_generation(idx, idx2, idx3, size, x, y, val3, "bcg")
                    print(self.blocks_collision_group)

    # updates the level
    # @params screen : screen variable stored in main.py to get size of the window
    # @param recoil : The recoil of the map
    # @param size : The size of the blocks
    def update(self, screen, recoil, size):
        self.blocks_group.empty()
        self.blocks_collision_group.empty()
        for idx, val in enumerate(self.map):
            for idx2, val2 in enumerate(val):
                for idx3, val3 in enumerate(val2):
                    x = ((idx - idx2) * size[0] / 2) + recoil[0]
                    y = (((idx + idx2) * size[1] / 4) - idx3 * (size[1] / 2)) + recoil[1]
                    self.choose_block_when_updating(idx, idx2, idx3, size, x, y, val3, "bg")
        for idx, val in enumerate(self.collision_map):
            for idx2, val2 in enumerate(val):
                for idx3, val3 in enumerate(val2):
                    x = ((idx - idx2) * size[0] / 2) + recoil[0]
                    y = (((idx + idx2) * size[1] / 4) - idx3 * (size[1] / 2)) + recoil[1]
                    self.choose_block_when_updating(idx, idx2, idx3, size, x, y, val3, "bcg")

    def choose_block_when_generation(self, idx, idx2, idx3, size, x, y, val3, group):
        if val3 != 0:
            if val3 == Block.GRASS or val3 == 1:
                grass = GrassBlock()
                grass.image = pygame.image.load("assets/images/blocks/isometric_0087.png")
                grass.image = pygame.transform.scale(grass.image, (size[0], size[1]))
                grass.rect = grass.image.get_rect()
                grass.rect.x = x
                grass.rect.y = y
                if group == "bg":
                    self.blocks_group.add(grass)
                    self.map[idx][idx2][idx3] = Block.GRASS_GENERATED
                elif group == "bcg":
                    self.blocks_collision_group.add(grass)
                    self.collision_map[idx][idx2][idx3] = Block.GRASS_GENERATED
            elif val3 == Block.BRICK or val3 == 3:
                brick = BrickBlock()
                brick.image = pygame.image.load("assets/images/blocks/isometric_0213.png")
                brick.image = pygame.transform.scale(brick.image, (size[0], size[1]))
                brick.rect = brick.image.get_rect()
                brick.rect.x = x
                brick.rect.y = y
                if group == "bg":
                    self.blocks_group.add(brick)
                    self.map[idx][idx2][idx3] = Block.BRICK_GENERATED
                elif group == "bcg":
                    self.blocks_collision_group.add(brick)
                    self.collision_map[idx][idx2][idx3] = Block.BRICK_GENERATED
            elif val3 == Block.STONE_BRICK or val3 == 5:
                stone_brick = StoneBrickBlock()
                stone_brick.image = pygame.image.load("assets/images/blocks/isometric_0055.png")
                stone_brick.image = pygame.transform.scale(stone_brick.image, (size[0], size[1]))
                stone_brick.rect = stone_brick.image.get_rect()
                stone_brick.rect.x = x
                stone_brick.rect.y = y
                if group == "bg":
                    self.blocks_group.add(stone_brick)
                    self.map[idx][idx2][idx3] = Block.STONE_BRICK_GENERATED
                elif group == "bcg":
                    self.blocks_collision_group.add(stone_brick)
                    self.collision_map[idx][idx2][idx3] = Block.STONE_BRICK_GENERATED
            elif val3 == Block.MAGMA or val3 == 7:
                magma = MagmaBlock()
                magma.image = pygame.image.load("assets/images/blocks/isometric_0036.png")
                magma.image = pygame.transform.scale(magma.image, (size[0], size[1]))
                magma.rect = magma.image.get_rect()
                magma.rect.x = x
                magma.rect.y = y
                if group == "bg":
                    self.blocks_group.add(magma)
                    self.map[idx][idx2][idx3] = Block.MAGMA_GENERATED
                elif group == "bcg":
                    self.blocks_collision_group.add(magma)
                    self.collision_map[idx][idx2][idx3] = Block.MAGMA_GENERATED

    def choose_block_when_updating(self, idx, idx2, idx3, size, x, y, val3, group):
        if val3 != 0:
            if val3 == Block.GRASS_GENERATED:
                grass = GrassBlock()
                grass.image = pygame.image.load("assets/images/blocks/isometric_0087.png")
                grass.image = pygame.transform.scale(grass.image, (size[0], size[1]))
                grass.rect.x = x
                grass.rect.y = y
                if group == "bg":
                    self.blocks_group.add(grass)
                elif group == "bcg":
                    self.blocks_collision_group.add(grass)
            elif val3 == Block.BRICK_GENERATED:
                brick = BrickBlock()
                brick.image = pygame.image.load("assets/images/blocks/isometric_0213.png")
                brick.image = pygame.transform.scale(brick.image, (size[0], size[1]))
                brick.rect.x = x
                brick.rect.y = y
                if group == "bg":
                    self.blocks_group.add(brick)
                elif group == "bcg":
                    self.blocks_collision_group.add(brick)
                self.map[idx][idx2][idx3] = Block.BRICK_GENERATED
            elif val3 == Block.STONE_BRICK_GENERATED:
                stone_brick = StoneBrickBlock()
                stone_brick.image = pygame.image.load("assets/images/blocks/isometric_0055.png")
                stone_brick.image = pygame.transform.scale(stone_brick.image, (size[0], size[1]))
                stone_brick.rect.x = x
                stone_brick.rect.y = y
                if group == "bg":
                    self.blocks_group.add(stone_brick)
                elif group == "bcg":
                    self.blocks_collision_group.add(stone_brick)
                self.map[idx][idx2][idx3] = Block.STONE_BRICK_GENERATED
            elif val3 == Block.MAGMA_GENERATED:
                magma = MagmaBlock()
                magma.image = pygame.image.load("assets/images/blocks/isometric_0036.png")
                magma.image = pygame.transform.scale(magma.image, (size[0], size[1]))
                magma.rect.x = x
                magma.rect.y = y
                if group == "bg":
                    self.blocks_group.add(magma)
                elif group == "bcg":
                    self.blocks_collision_group.add(magma)
                self.map[idx][idx2][idx3] = Block.MAGMA_GENERATED
