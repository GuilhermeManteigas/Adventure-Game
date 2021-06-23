
class Entity:
    def __init__(self, id, x, y, collision, entity_face):
        self.id = id
        self.x = x
        self.y = y
        self.collision = collision
        self.hitbox = 0
        self.entity_face = entity_face
        self.create_time = 0
        self.age = 0
        self.drop = False

    def update(self, time):
        if not self.drop:
            self.age = time - self.create_time
            if self.entity_face <= 4 :
                if self.age >= 4:
                    self.entity_face = 3
                elif self.age == 3:
                    self.entity_face = 2
                elif self.age == 2:
                    self.entity_face = 1
                else:
                    self.entity_face = 0

    def destroy(self):
        #if self.drop:
            self.id = 0
            self.collision = False
            self.hitbox = 0
            self.entity_face = 0
            self.create_time = 0
            self.age = 0
            self.drop = False
        #else:
        #    self.id += 100
        #    self.collision = False
        #    self.hitbox = 0
        #    self.entity_face = self.entity_face
        #    self.create_time = 0
        #    self.age = 0
        #    self.drop = True
