
class Drop:
    def __init__(self, x, y, id, quantity, day):
        self.x = x
        self.y = y
        self.id = id
        self.quantity = quantity
        self.face = self.face_calculator()
        self.creation_day = day

    def face_calculator(self):
        if self.quantity == 1:
            return 0
        elif self.quantity == 2:
            return 1
        elif self.quantity == 3:
            return 2
        elif self.quantity >= 4:
            return 3


