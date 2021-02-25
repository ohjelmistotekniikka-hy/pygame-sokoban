class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx=0, dy=0):
        self.x = self.x + dx
        self.y = self.y + dy

    def intersects(self, game_object):
        horizontal_intersection = self.x >= game_object.x and self.x < game_object.x + game_object.width
        vertical_intersection = self.y >= game_object.y and self.y < game_object.y + game_object.height

        return horizontal_intersection and vertical_intersection
