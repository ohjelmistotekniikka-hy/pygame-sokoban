import unittest
import pygame

from level import Level
from game_loop import GameLoop


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventLoop:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


LEVEL_MAP_1 = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 2, 3, 4, 1],
               [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP_1, CELL_SIZE)

    def test_can_complete_level(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
        ]

        game_loop = GameLoop(
            self.level_1,
            StubRenderer(),
            StubEventLoop(events),
            StubClock(),
            CELL_SIZE
        )

        game_loop.start()

        self.assertTrue(self.level_1.is_completed())
