import uuid

class Objet:
    def __init__(self, nom, poids, valeur):
        self.id = uuid.uuid4()
        self.nom = nom
        self.poids = poids
        self.valeur = valeur

    def __repr__(self):
        return f"Objet(id={self.id}, nom={self.nom}, poids={self.poids}, valeur={self.valeur})"

    def __str__(self):
        return f"{self.nom} (poids: {self.poids}, valeur: {self.valeur})"
    
// pomme = Objet("Pomme", 5, 1)
// print(pomme)
