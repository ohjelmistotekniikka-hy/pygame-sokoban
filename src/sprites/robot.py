import pygame
from load_image import load_image


class Robot(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, is_in_target=False):
        super().__init__()

        self.is_in_target = is_in_target

        self._images = self._load_images()

        self.image = self._images["robot"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.is_in_target:
            self.image = self._images["robot_in_target"]
        else:
            self.image = self._images["robot"]

    def _load_images(self):
        return {
            "robot": load_image("robot.png"),
            "robot_in_target": load_image("robot_in_target.png")
        }
