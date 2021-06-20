from entity import Entity

class Block:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.collision = False
        self.entity = Entity(0, False)
        self.hitbox = 0


