import pygame
import os

dirname = os.path.dirname(__file__)


def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
