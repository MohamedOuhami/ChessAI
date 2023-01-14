from pieces import piece
import pygame

# Initializing the class
class king(piece.piece):
    def __init__(self, color, x, y, value) -> None:
        super().__init__(color, x, y, value)
        self.sprite = pygame.image.load("sprites/king.png")
        self.spriterect = self.sprite.get_rect()