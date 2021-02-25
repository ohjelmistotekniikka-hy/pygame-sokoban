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


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP_1)
        self.level_2 = Level(LEVEL_MAP_2)

    def assert_coordinates_equal(self, game_object, x, y):
        self.assertEqual(game_object.x, x)
        self.assertEqual(game_object.y, y)

    def test_can_move_in_floor(self):
        robot = self.level_1.robot

        self.assert_coordinates_equal(robot.game_object, 3, 2)

        self.level_1.move_robot(dy=-1)
        self.assert_coordinates_equal(robot.game_object, 3, 1)

        self.level_1.move_robot(dx=-1)
        self.assert_coordinates_equal(robot.game_object, 2, 1)

    def test_can_not_move_through_walls(self):
        robot = self.level_1.robot

        self.assert_coordinates_equal(robot.game_object, 3, 2)

        self.level_1.move_robot(dx=1)
        self.assert_coordinates_equal(robot.game_object, 3, 2)

        self.level_1.move_robot(dy=1)
        self.assert_coordinates_equal(robot.game_object, 3, 2)

    def test_can_move_box(self):
        robot = self.level_1.robot
        box = self.level_1.boxes[0]

        self.assert_coordinates_equal(robot.game_object, 3, 2)

        self.level_1.move_robot(dx=-1)
        self.assert_coordinates_equal(robot.game_object, 2, 2)
        self.assert_coordinates_equal(box.game_object, 1, 2)

    def test_can_not_move_box_through_walls(self):
        robot = self.level_1.robot
        box = self.level_1.boxes[0]

        self.assert_coordinates_equal(robot.game_object, 3, 2)

        self.level_1.move_robot(dx=-1)
        self.assert_coordinates_equal(robot.game_object, 2, 2)
        self.assert_coordinates_equal(box.game_object, 1, 2)

        self.level_1.move_robot(dx=-1)
        self.assert_coordinates_equal(robot.game_object, 2, 2)
        self.assert_coordinates_equal(box.game_object, 1, 2)

    def test_can_not_move_box_through_boxes(self):
        robot = self.level_2.robot
        box_1 = self.level_2.boxes[0]
        box_2 = self.level_2.boxes[1]

        self.assert_coordinates_equal(robot.game_object, 3, 2)

        self.level_1.move_robot(dx=-1)
        self.assert_coordinates_equal(robot.game_object, 3, 2)
        self.assert_coordinates_equal(box_1.game_object, 1, 2)
        self.assert_coordinates_equal(box_2.game_object, 2, 2)


    def test_completed_status_is_correct(self):
        robot = self.level_1.robot
        box = self.level_1.boxes[0]

        self.assert_coordinates_equal(robot.game_object, 3, 2)
        self.assertFalse(self.level_1.is_completed())

        self.level_1.move_robot(dx=-1)
        self.assertTrue(self.level_1.is_completed())
