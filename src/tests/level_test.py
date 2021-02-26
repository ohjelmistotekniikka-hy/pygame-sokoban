import unittest

from level import Level

LEVEL_MAP_1 = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 2, 3, 4, 1],
               [1, 1, 1, 1, 1]]

LEVEL_MAP_2 = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 3, 3, 4, 1],
               [1, 1, 1, 1, 1]]

GRID_SIZE = 50


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP_1, GRID_SIZE)
        self.level_2 = Level(LEVEL_MAP_2, GRID_SIZE)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move_in_floor(self):
        robot = self.level_1.robot

        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)

        self.level_1.move_robot(dy=-GRID_SIZE)
        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, GRID_SIZE)

        self.level_1.move_robot(dx=-GRID_SIZE)
        self.assert_coordinates_equal(robot, 2 * GRID_SIZE, GRID_SIZE)

    def test_can_not_move_through_walls(self):
        robot = self.level_1.robot

        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)

        self.level_1.move_robot(dx=GRID_SIZE)
        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)

        self.level_1.move_robot(dy=GRID_SIZE)
        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)

    def test_can_move_box(self):
        robot = self.level_1.robot
        box = self.level_1.boxes.sprites()[0]

        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)

        self.level_1.move_robot(dx=-GRID_SIZE)
        self.assert_coordinates_equal(robot, 2 * GRID_SIZE, 2 * GRID_SIZE)
        self.assert_coordinates_equal(box, GRID_SIZE, 2 * GRID_SIZE)

    def test_can_not_move_box_through_walls(self):
        robot = self.level_1.robot
        box = self.level_1.boxes.sprites()[0]

        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)

        self.level_1.move_robot(dx=-GRID_SIZE)
        self.assert_coordinates_equal(robot, 2 * GRID_SIZE, 2 * GRID_SIZE)
        self.assert_coordinates_equal(box, GRID_SIZE, 2 * GRID_SIZE)

        self.level_1.move_robot(dx=-GRID_SIZE)
        self.assert_coordinates_equal(robot, 2 * GRID_SIZE, 2 * GRID_SIZE)
        self.assert_coordinates_equal(box, GRID_SIZE, 2 * GRID_SIZE)

    def test_can_not_move_box_through_boxes(self):
        robot = self.level_2.robot
        box_1 = self.level_2.boxes.sprites()[0]
        box_2 = self.level_2.boxes.sprites()[1]

        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)

        self.level_1.move_robot(dx=-GRID_SIZE)
        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)
        self.assert_coordinates_equal(box_1, GRID_SIZE, 2 * GRID_SIZE)
        self.assert_coordinates_equal(box_2, 2 * GRID_SIZE, 2 * GRID_SIZE)

    def test_completed_status_is_correct(self):
        robot = self.level_1.robot
        box = self.level_1.boxes.sprites()[0]

        self.assert_coordinates_equal(robot, 3 * GRID_SIZE, 2 * GRID_SIZE)
        self.assertFalse(self.level_1.is_completed())

        self.level_1.move_robot(dx=-GRID_SIZE)
        self.assertTrue(self.level_1.is_completed())
