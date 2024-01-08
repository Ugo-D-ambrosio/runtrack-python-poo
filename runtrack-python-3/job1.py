class Ville:
    def __init__(self, nom, nb_habitants):
        self._nom = nom
        self._nb_habitants = nb_habitants

    def get_nom(self):
        return self._nom

    def get_nb_habitants(self):
        return self._nb_habitants

    def augmenter_population(self):
        self._nb_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville
        self._ville.augmenter_population()

    def get_nom(self):
        return self._nom

    def get_age(self):
        return self._age

    def get_ville(self):
        return self._ville


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Nombre d'habitants de {paris.get_nom()}: {paris.get_nb_habitants()}")
print(f"Nombre d'habitants de {marseille.get_nom()}: {marseille.get_nb_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Nombre d'habitants de {paris.get_nom()} après l'arrivée de personnes: {paris.get_nb_habitants()}")
print(f"Nombre d'habitants de {marseille.get_nom()} après l'arrivée de personnes: {marseille.get_nb_habitants()}")
