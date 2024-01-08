class Animal:
    def __init__(self, prenom=""):
        self.age = 0
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

mon_animal = Animal("Rex")

print("Âge initial de l'animal :", mon_animal.age)

mon_animal.vieillir()

print("Âge de l'animal après vieillissement :", mon_animal.age)

class Animal:
    def __init__(self):
        self.age = 0
        self.nom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.nom = nom

mon_animal = Animal()

mon_animal.nommer("Rex")

print("Nom de l'animal :", mon_animal.nom)
