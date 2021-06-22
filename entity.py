
class Entity:
    def __init__(self, id, collision, entity_face):
        self.id = id
        self.collision = collision
        self.hitbox = 0
        self.entity_face = entity_face
        self.create_time = 0
        self.age = 0

    def update(self, time):
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


