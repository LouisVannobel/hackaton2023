from tkinter import *

class Base:
    def __init__(self):
        self.stockage = []

    def ajouter_objet(self, objet):
        self.stockage.append(objet)

# Création d'une base
base = Base()

# Simule l'ajout d'objets à la base par les robots
base.ajouter_objet("Objet1")


# On crée une fenêtre, racine de notre interface
Fenetre = Tk()

# On crée un Canvas pour représenter la zone de stockage
zone_stockage = Canvas(Fenetre, width=500, height=500, bg="white", bd=8)
zone_stockage.pack()  # Affiche le Canvas

# On ajoute des éléments pour représenter les objets stockés
x, y = 50, 50
for objet in base.stockage:
    zone_stockage.create_rectangle(x, y, x + 50, y + 50, fill="blue")
    x += 100

# On démarre la boucle Tkinter qui s'interrompt quand on ferme la fenêtre
Fenetre.mainloop()
