class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self._titre = titre
        self._description = description
        self._statut = statut

    def get_titre(self):
        return self._titre

    def get_description(self):
        return self._description

    def get_statut(self):
        return self._statut

    def marquer_comme_finie(self):
        self._statut = "terminée"


class ListeDeTaches:
    def __init__(self):
        self._taches = []

    def ajouter_tache(self, tache):
        self._taches.append(tache)

    def supprimer_tache(self, tache):
        self._taches.remove(tache)

    def afficher_liste(self):
        for tache in self._taches:
            print(f"Tâche : {tache.get_titre()}, Statut : {tache.get_statut()}")

    def filter_liste(self, statut):
        filtered_list = [tache for tache in self._taches if tache.get_statut() == statut]
        return filtered_list


# Création de tâches
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 5", "à faire")
tache3 = Tache("Nettoyer la maison", "Aspirer et faire la poussière", "à faire")

liste_taches = ListeDeTaches()

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

print("Liste de toutes les tâches :")
liste_taches.afficher_liste()

tache2.marquer_comme_finie()

print("\nListe des tâches à faire :")
taches_a_faire = liste_taches.filter_liste("à faire")
for tache in taches_a_faire:
    print(f"Tâche : {tache.get_titre()}, Statut : {tache.get_statut()}")
