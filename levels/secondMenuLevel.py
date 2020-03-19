import pygame

from blocks.block import Block
from levels.isometricLevel import IsometricLevel


# class which contains the second menu (IsometricLevel)
class SecondMenuLevel(IsometricLevel):

    # construct method
    # @param game : instance of the class Game
    def __init__(self):
        super().__init__()
        self.map = [

            [[1], [1], [1],             [1],             [1],             [1],             [1],             [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1],             [1],             [1],             [1],             [1],             [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1, 3, 3, 3, 3], [1, 3, 0, 0, 3], [1, 3, 0, 0, 3], [1, 3, 0, 0, 3], [1, 3, 3, 3, 3], [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1, 3, 0, 0, 3], [1, 7],          [1, 5],          [1],             [1],             [1, 3], [1], [1], [1] , [1] , [1]],
            [[1], [1], [1, 3, 0, 0, 3], [1, 5],          [1, 5],          [1],             [1],             [1, 3], [1], [1], [1] , [1] , [1]],
            [[1], [1], [1, 3, 0, 0, 3], [1],             [1],             [1],             [1],             [1, 3], [1], [1], [1] , [1] , [1]],
            [[1], [1], [1, 3, 3, 3, 3], [1],             [1],             [1],             [1, 3],          [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1],             [1, 3],          [1, 3],          [1, 3],          [1],             [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1],             [1],             [1],             [1],             [1],             [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1],             [1],             [1],             [1],             [1],             [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1],             [1],             [1],             [1],             [1],             [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1],             [1],             [1],             [1],             [1],             [1],    [1], [1], [1] , [1] , [1]],
            [[1], [1], [1],             [1],             [1],             [1],             [1],             [1],    [1], [1], [1] , [1] , [1]]

        ]
