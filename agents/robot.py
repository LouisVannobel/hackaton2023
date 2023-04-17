from hackaton2023.environnement.carte import Tableau as Carte
from hackaton2023.environnement.base import Base
import uuid
import random

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
        self.energie_par_deplacement = 1
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
            if self.equipe is not None:
                self.equipe.gagner_argent(objet.valeur)
            return True
        return False
        
    def se_deplacer_vers_borne(self, borne):
        borne_row, borne_col = borne.row, borne.column
        dist_row, dist_col = abs(borne_row - self.row), abs(borne_col - self.column)
        if dist_row > dist_col:
            # se déplace verticalement
            if borne_row < self.row:
                self.row -= 1
            elif borne_row > self.row:
                self.row += 1
        else:
            # se déplace horizontalement
            if borne_col < self.column:
                self.column -= 1
            elif borne_col > self.column:
                self.column += 1

        self.energie -= self.energie_par_deplacement
        
    def distance_jusqu_a_borne(self):
        distance_min = float('inf')
        borne_proche = None
        for borne in self.carte.bornes_recharge:
            distance = abs(borne.row - self.row) + abs(borne.column - self.column)
            if distance < distance_min:
                distance_min = distance
                borne_proche = borne
        return distance_min, borne_proche
    
    def se_deplacer_vers_objet(self, objet, base):
    distance_min, borne_proche = self.distance_jusqu_a_borne()
    energie_requise = distance_min * self.energie_par_deplacement
    if self.energie < energie_requise:
        self.se_deplacer_vers_borne(borne_proche)
        self.recharger()

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
            base_row, base_col = base.row, base.column
            dist_row, dist_col = abs(base_row - self.row), abs(base_col - self.column)
            if dist_row > dist_col:
                # se déplace verticalement
                if base_row < self.row:
                    self.row -= 1
                elif base_row > self.row:
                    self.row += 1
            else:
                # se déplace horizontalement
                if base_col < self.column:
                    self.column -= 1
                elif base_col > self.column:
                    self.column += 1

            # Si le robot a atteint la base, dépose l'objet et met à jour les points de l'équipe
            if self.row == base_row and self.column == base_col:
                self.ajouter_objet(objet, base)

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
        self.points = 0
        self.argent = 0

    def ajouter_robot(self, robot):
        self.robots.append(robot)
        robot.assigner_equipe(self)

    def gagner_argent(self, montant):
        self.argent += montant
        self.points += montant

    def accomplir_tache(self, points_tache):
        self.points += points_tache
