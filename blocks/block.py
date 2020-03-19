from enum import Enum


# enum which contains every block of the game
class Block(Enum):

    AIR = 0
    GRASS = 1
    GRASS_GENERATED = 2
    BRICK = 3
    BRICK_GENERATED = 4
    STONE_BRICK = 5
    STONE_BRICK_GENERATED = 6
    MAGMA = 7
    MAGMA_GENERATED = 8
