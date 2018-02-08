class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        self.eat()
        print('moving')
    def eat(self):
        print('eating food')

class Mammals(Animals):
    def feed(self):
        print('feeding young')

class Giraffes(Mammals):
    def __init__(self, spots):
        self.spots = spots
    def showSpots(self):
        print('I have %s spots' % self.spots)


