class Heart:
    def __init__(self, heart_use):
        self.heart_use =heart_use

    @property
    def state(self):
        if self.heart_use > 70:
            return "high blood pressure"
        else:
            return "feeling good"

class Brain:
    def __init__(self, brain_use):
        self.brain_use = brain_use

    @property
    def state(self):
        if self.brain_use > 90:
            return "tired"
        else:
            return "rested"
        
class Leg:
    def __init__(self, moving_speed):
        self.moving_speed = moving_speed

    @property
    def state(self):
        if self.moving_speed > 10:
            return "running"
        elif self.moving_speed > 0:
            return "walking"
        else:
            return "standing"

class Person:
    def __init__(self, heart_use, brain_use, moving_speed):
        self.heart = Heart(heart_use)
        self.brain = Brain(brain_use)
        self.moving_speed = moving_speed
        self.leg = None

    def set_leg(self):
        self.leg = Leg(self.moving_speed)
        
person = Person(75, 85, 12)
person.set_leg()
