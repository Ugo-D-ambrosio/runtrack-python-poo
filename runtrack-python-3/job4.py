class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} (n°{self.numero}, {self.position}):")
        print(f"Buts marqués : {self.buts_marques}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes reçus : {self.cartons_jaunes}")
        print(f"Cartons rouges reçus : {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, nom_joueur, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges
                print(f"Statistiques de {joueur.nom} mises à jour.")

joueur1 = Joueur("John", 10, "Attaquant")
joueur2 = Joueur("Alice", 5, "Milieu de terrain")
joueur3 = Joueur("Bob", 3, "Défenseur")

equipe1 = Equipe("Équipe A")
equipe2 = Equipe("Équipe B")

equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)
equipe2.ajouter_joueur(joueur3)

equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

joueur1.marquer_un_but()
joueur2.effectuer_une_passe_decisive()
joueur3.recevoir_un_carton_jaune()

equipe1.mettre_a_jour_statistiques_joueur("John", buts=1)
equipe1.mettre_a_jour_statistiques_joueur("Alice", passes=1)
equipe2.mettre_a_jour_statistiques_joueur("Bob", jaunes=1)

equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()
