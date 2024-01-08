class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return f"Point(x: {self.x}, y: {self.y})"

    def afficherX(self):
        return f"x: {self.x}"

    def afficherY(self):
        return f"y: {self.y}"

    def changerX(self, new_x):
        self.x = new_x

    def changerY(self, new_y):
        self.y = new_y

point = Point(5, 10)

print(point.afficherLesPoints())

point.changerX(20)
point.changerY(30)

print(point.afficherLesPoints())

