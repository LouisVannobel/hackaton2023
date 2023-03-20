import uuid
import random

class Robot:
    def __init__(self, nom, vitesse, capacite, carte):
        self.id = uuid.uuid4()
        self.nom = nom
        self.vitesse = vitesse
        self.capacite = capacite
        self.carte = carte
        self.row, self.column = self.position_aleatoire_robot()
        self.objets_portes = []

    def position_aleatoire_robot(self):
        row = random.randint(0, self.carte.rows - 1)
        column = random.randint(0, self.carte.columns - 1)
        return row, column

    def detecter_objet(self, liste_objets):
        objets_detectes = []
        for objet in liste_objets:
            if objet.row == self.row and objet.column == self.column:
                objets_detectes.append(objet)
        return objets_detectes

    def prendre_objet(self, objet):
        if len(self.objets_portes) < self.capacite:
            self.objets_portes.append(objet)
            return True
        return False

    def deposer_objet(self, objet):
        if objet in self.objets_portes:
            self.objets_portes.remove(objet)
            return True

    def compter_objets(self):
        return len(self.objets_portes)
        return False
