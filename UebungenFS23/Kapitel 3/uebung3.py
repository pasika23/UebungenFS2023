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
        return f'Punkt({self.x}, {self.y})'  

    def distanz(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5  

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
        return 2 * self.radius * math.pi
    
    def __str__(self):
        return f'Kreis M = {self.mittelpunkt} und r = {self.radius}'  
    
class Dreieck(Figur):
    def __init__(self, ax, ay, bx, by, cx, cy):
        super().__init__("Dreieck")
        self.A = Punkt(ax, ay)
        self.B = Punkt(bx, by)
        self.C = Punkt(cx, cy)

    def umfang(self):
        return self.A.distanz(self.B) + self.B.distanz(self.C) + self.C.distanz(self.A)      
    
    def __str__(self):
        return f'Dreieck mit A = {self.A}, B = {self.B}  und C = {self.C}' 
    
class Viereck(Figur):
    def __init__(self, x1, y1, x2, y2):
        super().__init__("Viereck")
        self.A = Punkt(x1, y1)
        self.B = Punkt(x2, y1)
        self.C = Punkt(x2, y2)
        self.D = Punkt(x1, y2)

    def umfang(self):
        return self.A.distanz(self.B) + self.B.distanz(self.C) + self.C.distanz(self.D) + self.D.distanz(self.A)      
    
    def __str__(self):
        return f'Viereck {self.A}-{self.C}'
    
a = Dreieck(0,0,0,4,5,6) 
print(a)
print(a.umfang())

b= Viereck(0,0,3,3)
print(b)
print(b.umfang())