import pygame
import os

dirname = os.path.dirname(__file__)


def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, 'assets', filename)
    )


class PygameRenderer:
    def __init__(self, display, scale, level):
        self._display = display
        self._scale = scale
        self._level = level
        self._images = {}
        self._load_images()

    def render_display(self):
        self._display.fill((0, 0, 0))

        for wall in self._level.walls:
            self._render_wall(wall)

        for floor in self._level.floors:
            self._render_floor(floor)

        for target in self._level.targets:
            self._render_target(target)

        for box in self._level.boxes:
            self._render_box(box)

        self._render_robot()

        pygame.display.flip()

    def _load_images(self):
        self._images = {
            "floor": load_image("floor.png"),
            "wall": load_image("wall.png"),
            "target": load_image("target.png"),
            "robot": load_image("robot.png"),
            "box": load_image("box.png"),
            "robot_in_target": load_image("robot_in_target.png"),
            "box_in_target": load_image("box_in_target.png"),
        }

    def _render_game_object(self, game_object, image_name):
        self._display.blit(
            self._images[image_name],
            (
                game_object.x * self._scale,
                game_object.y * self._scale,
            )
        )

    def _render_wall(self, wall):
        self._render_game_object(wall.game_object, "wall")

    def _render_floor(self, floor):
        self._render_game_object(floor.game_object, "floor")

    def _render_target(self, target):
        self._render_game_object(target.game_object, "target")

    def _render_robot(self):
        targets = self._level.targets
        robot = self._level.robot

        intersecting_targets = [
            target for target in targets if robot.game_object.intersects(target.game_object)
        ]

        if len(intersecting_targets) > 0:
            self._render_game_object(
                robot.game_object,
                "robot_in_target"
            )
        else:
            self._render_game_object(robot.game_object, "robot")

    def _render_box(self, box):
        targets = self._level.targets

        intersecting_targets = [
            target for target in targets if box.game_object.intersects(target.game_object)
        ]

        if len(intersecting_targets) > 0:
            self._render_game_object(box.game_object, "box_in_target")
        else:
            self._render_game_object(box.game_object, "box")
