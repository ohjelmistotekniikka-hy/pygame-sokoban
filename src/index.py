import pygame

from level import Level
from game_logic import GameLogic
from pygame_event_loop import PygameEventLoop
from pygame_renderer import PygameRenderer


LEVEL_MAP_1 = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 2, 3, 4, 1],
               [1, 1, 1, 1, 1]]

LEVEL_MAP_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
               [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
               [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

SCALE = 50


def main():
    level_map = LEVEL_MAP_2
    height = len(level_map)
    width = len(level_map[0])
    display_height = height * SCALE
    display_width = width * SCALE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Sokoban")

    level = Level(level_map)
    event_loop = PygameEventLoop()
    renderer = PygameRenderer(display, SCALE, level)
    game_logic = GameLogic(level, renderer, event_loop)

    pygame.init()
    game_logic.start_game_loop()


if __name__ == "__main__":
    main()
