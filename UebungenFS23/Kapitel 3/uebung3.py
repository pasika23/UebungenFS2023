import math

class Figur:
    def __init__(self, name):
        self.name = name
    
    def umfang(self):
        return 0
    
    def __str__(self):
        return self.name
    
class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f'Punkt ({self.x}, {self.y})'    

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
        return self.radius**2 * math.pi
    
    def __str__(self):
        return f'Kreis M = {self.mittelpunkt} und r = {self.radius}'  