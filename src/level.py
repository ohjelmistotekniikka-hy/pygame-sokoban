import pygame
from sprites.robot import Robot
from sprites.box import Box
from sprites.floor import Floor
from sprites.target import Target
from sprites.wall import Wall


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.robot = None
        self.walls = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def update(self, current_time):
        for box in self.boxes:
            box.is_in_target = self._box_is_in_target(box)

        self.robot.is_in_target = self._robot_is_in_target()

        self.boxes.update()
        self.robot.update()

    def move_robot(self, dx=0, dy=0):
        if not self._robot_can_move(dx, dy):
            return

        self.robot.rect.move_ip(dx, dy)

        colliding_boxes = self._get_colliding_boxes(self.robot)

        if colliding_boxes:
            colliding_boxes[0].rect.move_ip(dx, dy)

    def is_completed(self):
        for box in self.boxes:
            if not self._box_is_in_target(box):
                return False

        return True

    def _box_is_in_target(self, box):
        return len(self._get_colliding_targets(box)) > 0

    def _robot_is_in_target(self):
        return len(self._get_colliding_targets(self.robot)) > 0

    def _get_colliding_walls(self, sprite):
        return pygame.sprite.spritecollide(sprite, self.walls, False)

    def _get_colliding_boxes(self, sprite):
        return pygame.sprite.spritecollide(sprite, self.boxes, False)

    def _get_colliding_targets(self, sprite):
        return pygame.sprite.spritecollide(sprite, self.targets, False)

    def _robot_can_move(self, dx=0, dy=0):
        self.robot.rect.move_ip(dx, dy)

        colliding_walls = self._get_colliding_walls(self.robot)
        colliding_boxes = self._get_colliding_boxes(self.robot)
        first_colliding_box = colliding_boxes[0] if colliding_boxes else None

        can_move = not colliding_walls and (
            first_colliding_box is None or self._can_move(
                first_colliding_box, dx, dy
            )
        )

        self.robot.rect.move_ip(-dx, -dy)

        return can_move

    def _can_move(self, sprite, dx=0, dy=0):
        sprite.rect.move_ip(dx, dy)

        colliding_walls = self._get_colliding_walls(sprite)
        colliding_boxes = self._get_colliding_boxes(sprite)

        if isinstance(sprite, Box):
            colliding_boxes.remove(sprite)

        can_move = not colliding_walls and not colliding_boxes

        sprite.rect.move_ip(-dx, -dy)

        return can_move

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.targets.add(Target(normalized_x, normalized_y))
                elif cell == 3:
                    self.boxes.add(Box(normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 4:
                    self.robot = Robot(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.targets,
            self.boxes,
            self.robot
        )
