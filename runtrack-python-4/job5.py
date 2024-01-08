class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14159 * self.radius ** 2

mon_rectangle = Rectangle(5, 3)

mon_cercle = Cercle(4)

aire_rectangle = mon_rectangle.aire()
print(f"L'aire du rectangle est : {aire_rectangle}")

aire_cercle = mon_cercle.aire()
print(f"L'aire du cercle est : {aire_cercle}")
