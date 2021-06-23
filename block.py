from entity import Entity

class Block:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.collision = False
        self.entity = Entity(0, x, y, False, 0, [False])
        self.hitbox = 0
        self.block_face = 0 # 0 to 8 representing the position blocks
        self.height = 1 # 0 for liquids 1 for normal blocks


