
from blocks.Block import Block
from levels.isometricLevel import IsometricLevel


# class which contains the second menu (IsometricLevel)
class SecondMenuLevel(IsometricLevel):

    # construct method
    def __init__(self):
        super().__init__()
        self.map = [

            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]],
            [[Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS], [Block.GRASS]]

        ]
