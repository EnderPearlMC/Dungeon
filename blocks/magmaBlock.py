import pygame


# sprite magma block
class MagmaBlock(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/blocks/isometric_0036.png")
        self.image = pygame.transform.scale(self.image, (100, 116))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
