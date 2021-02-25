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
        return (self.x < game_object.x + game_object.width) and (self.x + game_object.width > game_object.x) and (self.y < game_object.y + game_object.height) and (self.y + self.height > game_object.y)
