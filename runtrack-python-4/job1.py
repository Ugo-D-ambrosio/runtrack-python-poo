class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"Âge de la personne : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
eleve = Eleve()

eleve.afficherAge()
