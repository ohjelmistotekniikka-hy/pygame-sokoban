import pygame
from level import Level
from game_loop import GameLoop
from event_loop import EventLoop
from renderer import Renderer
from clock import Clock

LEVEL_MAP_1 = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 2, 3, 4, 1],
               [1, 1, 1, 1, 1]]

LEVEL_MAP_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 5, 1],
               [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
               [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50


def main():
    level_map = LEVEL_MAP_2
    height = len(level_map)
    width = len(level_map[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Sokoban")

    level = Level(level_map, CELL_SIZE)

    event_loop = EventLoop()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_loop, clock, CELL_SIZE)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
