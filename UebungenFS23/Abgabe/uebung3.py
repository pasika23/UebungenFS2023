import math

class Figur:
    def __init__(self, name):
        self.name = name
    
    def umfang(self):
        return 0
    
    def __str__(self):
        return self.name
    
# -------------------------------------------------------------------------------------------------------

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f'Punkt({self.x}, {self.y})'  

    def distanz(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5  

# -------------------------------------------------------------------------------------------------------

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
        return 2 * self.radius * math.pi
    
    def __str__(self):
        return f'Kreis M = {self.mittelpunkt} und r = {self.radius}'  
    
# -------------------------------------------------------------------------------------------------------

class Dreieck(Figur):
    def __init__(self, ax, ay, bx, by, cx, cy):
        super().__init__("Dreieck")
        self.A = Punkt(ax, ay)  # oder direkt self.A = A
        self.B = Punkt(bx, by)
        self.C = Punkt(cx, cy)

    def umfang(self):
        return self.A.distanz(self.B) + self.B.distanz(self.C) + self.C.distanz(self.A)      
    
    def __str__(self):
        return f'Dreieck mit A = {self.A}, B = {self.B}  und C = {self.C}' 
    
# -------------------------------------------------------------------------------------------------------

class Rechteck(Figur):
    def __init__(self, Pmin,Pmax):
        super().__init__("Rechteck")
        self.Pmin = Pmin
        self.Pmax = Pmax
        
    def umfang(self):
        return 2 * abs(self.Pmax.x - self.Pmin.x) + 2 * abs(self.Pmax.y - self.Pmin.y)
    
    def __str__(self):
        return f'Rechteck: {self.Pmin},{self.Pmax}'
    
# -------------------------------------------------------------------------------------------------------

class Polygon(Figur):
    def __init__(self, Punktliste):
        super().__init__("Polygon")
        self.pl = Punktliste
        

    def umfang(self):
        u = 0
        for p in self.pl:
            if p >= len(self.pl) - 1:
                a = self.pl[p].distanz(self.pl[p+1])
                u = u + a

        return u
    
    def __str__(self):
        s = f'Polygon: '
        for punkt in self.pl:
            s = s + f'{punkt}'
        return s
    
# -------------------------------------------------------------------------------------------------------

P1 = Punkt(0,0)
P2 = Punkt(3,1)


a = Dreieck(0,0,0,4,5,6) 
print(a)
print(a.umfang())

r = Rechteck(P1,P2)
print(r.umfang())

polygon = [Punkt(1,1),Punkt(2,4),Punkt(3,3.4),Punkt(4,4),Punkt(4,1),Punkt(1,1)]
print(polygon)