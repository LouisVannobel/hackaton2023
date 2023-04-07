import uuid
import random
from base import Base

class Robot:
    def __init__(self, nom, vitesse, capacite, carte, equipe=None, energie_max=100):
        self.id = uuid.uuid4()
        self.nom = nom
        self.vitesse = vitesse
        self.capacite = capacite
        self.carte = carte
        self.row, self.column = self.position_aleatoire_robot()
        self.objets_portes = []
        self.energie = energie_max
        self.energie_max = energie_max
        self.equipe = equipe

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
        return False

    def compter_objets(self):
        return len(self.objets_portes)

    def ajouter_objet(self, objet, base):
        if self.deposer_objet(objet):
            base.ajouter_objet(objet)
            return True
        return False

    def se_deplacer_vers_objet(self, objet, base):
        # Vérifie si le robot transporte des objets et les dépose à la base
        for obj in self.objets_portes:
            self.deposer_objet(obj)
            base.ajouter_objet(obj)

        obj_row, obj_col = objet.row, objet.column
        dist_row, dist_col = abs(obj_row - self.row), abs(obj_col - self.column)
        if dist_row > dist_col:
            # se déplace verticalement
            if obj_row < self.row:
                self.row -= 1
            elif obj_row > self.row:
                self.row += 1
        else:
            # se déplace horizontalement
            if obj_col < self.column:
                self.column -= 1
            elif obj_col > self.column:
                self.column += 1

        # Si le robot a atteint l'objet cible, le récupère et le ramène à la base
        if self.row == obj_row and self.column == obj_col:
            if self.prendre_objet(objet):
                self.se_deplacer_vers_objet(base, None)

    def assigner_equipe(self, equipe):
        self.equipe = equipe
    
    def recharger(self):
        for borne in self.carte.bornes_recharge:
            if borne.row == self.row and borne.column == self.column:
                self.energie = self.energie_max
                return True
        return False

class Equipe:
    def __init__(self, id):
        self.id = id
        self.robots = []

    def ajouter_robot(self, robot):
        self.robots.append(robot)
        robot.assigner_equipe(self)
