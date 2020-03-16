import pygame


# sprite grass block
class GrassBlock(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/blocks/isometric_0087.png")
        self.image = pygame.transform.scale(self.image, (100, 116))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
