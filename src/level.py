from game_object import GameObject
from robot import Robot
from box import Box
from floor import Floor
from target import Target
from wall import Wall


class Level:
    def __init__(self, level_map):
        self.robot = None
        self.walls = []
        self.targets = []
        self.floors = []
        self.boxes = []

        self._initialize_game_objects(level_map)

    def move_robot(self, dx=0, dy=0):
        if not self._robot_can_move(dx, dy):
            return

        self.robot.game_object.move(dx, dy)

        intersecting_box = self._get_intersecting_box(self.robot.game_object)

        if intersecting_box is not None:
            intersecting_box.game_object.move(dx, dy)

    def is_completed(self):
        for target in self.targets:
            intersecting_box = self._get_intersecting_box(target.game_object)

            if intersecting_box is None:
                return False

        return True

    def _get_intersecting_wall(self, game_object):
        intersecting_walls = [
            wall for wall in self.walls if wall.game_object.intersects(game_object) and wall.game_object != game_object
        ]

        return intersecting_walls[0] if len(intersecting_walls) > 0 else None

    def _get_intersecting_box(self, game_object):
        intersecting_boxes = [
            box for box in self.boxes if box.game_object.intersects(game_object) and box.game_object != game_object
        ]

        return intersecting_boxes[0] if len(intersecting_boxes) > 0 else None

    def _box_can_move(self, box, dx=0, dy=0):
        box.game_object.move(dx, dy)

        intersecting_wall = self._get_intersecting_wall(box.game_object)

        intersecting_box = self._get_intersecting_box(box.game_object)

        can_move = intersecting_wall is None and intersecting_box is None

        box.game_object.move(-dx, -dy)

        return can_move

    def _robot_can_move(self, dx=0, dy=0):
        self.robot.game_object.move(dx, dy)

        intersecting_wall = self._get_intersecting_wall(self.robot.game_object)

        intersecting_box = self._get_intersecting_box(self.robot.game_object)

        can_move = intersecting_wall is None and (
            intersecting_box is None or self._box_can_move(intersecting_box, dx, dy))

        self.robot.game_object.move(-dx, -dy)

        return can_move

    def _initialize_game_objects(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                square = level_map[y][x]

                if square == 0:
                    self.floors.append(Floor(GameObject(x, y, 1, 1)))
                elif square == 1:
                    self.walls.append(Wall(GameObject(x, y, 1, 1)))
                elif square == 2:
                    self.targets.append(Target(GameObject(x, y, 1, 1)))
                elif square == 3:
                    self.boxes.append(Box(GameObject(x, y, 1, 1)))
                    self.floors.append(Floor(GameObject(x, y, 1, 1)))
                elif square == 4:
                    self.robot = Robot(GameObject(x, y, 1, 1))
                    self.floors.append(Floor(GameObject(x, y, 1, 1)))
