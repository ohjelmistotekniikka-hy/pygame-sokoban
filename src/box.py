import pygame
from load_image import load_image


class Box(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, is_in_target=False):
        super().__init__()

        self.is_in_target = is_in_target

        self._images = self._load_images()

        self.image = self._images["box"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        current_x = self.rect.x
        current_y = self.rect.y

        if self.is_in_target:
            self.image = self._images["box_in_target"]
        else:
            self.image = self._images["box"]

        self.rect = self.image.get_rect()
        self.rect.x = current_x
        self.rect.y = current_y

    def _load_images(self):
        return {
            "box": load_image("box.png"),
            "box_in_target": load_image("box_in_target.png")
        }
