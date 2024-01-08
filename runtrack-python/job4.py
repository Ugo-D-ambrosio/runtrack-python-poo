class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}"

personne1 = Personne("Dupont", "Jean Dupont")
personne2 = Personne("Martin", "Alice Martin")
personne3 = Personne("Durand", "Pierre Durand")

presentation1 = personne1.se_presenter()
presentation2 = personne2.se_presenter()
presentation3 = personne3.se_presenter()

print(presentation1)
print(presentation2)
print(presentation3)
