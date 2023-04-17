from tkinter import *
from PIL import Image, ImageTk  # Importer les modules pour travailler avec les images

class Base:
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column
        self.stockage = []

    def ajouter_objet(self, objet):
        self.stockage.append(objet)
        
    def compter_objets(self):
        return len(self.stockage)

# Création d'une base
base = Base()

# Simule l'ajout d'objets à la base par les robots
base.ajouter_objet("Objet1")

# Charger l'image
image = Image.open("entrepot.jpg")
image = image.resize((50, 50))  # Redimensionner l'image si nécessaire
image = ImageTk.PhotoImage(image)  # Convertir l'image en format Tkinter

# On crée une fenêtre, racine de notre interface
Fenetre = Tk()

# On crée un Canvas pour représenter la zone de stockage
zone_stockage = Canvas(Fenetre, width=500, height=500, bg="white", bd=8)
zone_stockage.pack()  # Affiche le Canvas

# On ajoute des éléments pour représenter les objets stockés
x, y = 50, 50
for objet in base.stockage:
    zone_stockage.create_image(x, y, image=image, anchor="nw")  # Ajouter l'image au canvas
    x += 100

# On démarre la boucle Tkinter qui s'interrompt quand on ferme la fenêtre
Fenetre.mainloop()

