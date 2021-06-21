
class Entity:
    def __init__(self, id, collision):
        self.id = id
        self.collision = collision
        self.hitbox = 0
        self.entity_face = 0
        self.create_time = 0

    def update(self, time):
        if self.create_time >= 3:
            self.entity_face = 2
        elif self.create_time == 2:
            self.entity_face = 1
        else:
            self.entity_face = 0


