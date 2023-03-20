import uuid
import random

class Objet:
    def __init__(self, nom, poids, valeur, carte):
        self.id = uuid.uuid4()
        self.nom = nom
        self.poids = poids
        self.valeur = valeur
        self.row, self.column = self.position_aleatoire_objet(carte)

    def __repr__(self):
        return f"Objet(id={self.id}, nom={self.nom}, poids={self.poids}, valeur={self.valeur})"

    def __str__(self):
        return f"{self.nom} (poids: {self.poids}, valeur: {self.valeur})"

    def position_aleatoire_objet(self, carte):
        row = random.randint(0, carte.rows - 1)
        column = random.randint(0, carte.columns - 1)
        return row, column


# Exemple d'utilisation
# carte = Carte(rows=30, columns=30)
# pomme = Objet("Pomme", 5, 1, carte)
# print(pomme)
