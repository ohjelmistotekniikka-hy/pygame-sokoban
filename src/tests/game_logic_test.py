import unittest
import pygame

from level import Level
from game_logic import GameLogic


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventLoop:
    def __init__(self, events):
        self._events = events

    def get_event(self):
        return self._events


class StubRenderer:
    def render_display(self):
        pass


LEVEL_MAP_1 = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 2, 3, 4, 1],
               [1, 1, 1, 1, 1]]


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP_1)

    def assert_coordinates_equal(self, game_object, x, y):
        self.assertEqual(game_object.x, x)
        self.assertEqual(game_object.y, y)

    def test_can_complete_level(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
        ]

        game_logic = GameLogic(
            self.level_1,
            StubRenderer(),
            StubEventLoop(events)
        )

        game_logic.start_game_loop()

        self.assertTrue(self.level_1.is_completed())
