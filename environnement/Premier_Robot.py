import tkinter as tk # On importe Tkinter 
# On crée une fenêtre, racine de notre interface
Fenetre = tk.Tk() # Dans Fenetre nous allons creer un objet type Canvas qui se nomme zone_dessin # Nous donnons des valeurs aux proprietes "width", "height", "bg", "bd" 

# Créer une image de fond (la map)
map1 = tk.PhotoImage(file="fondcarte.png")
# Créer un Canvas et ajouter l'image de fond
zone_dessin = tk.Canvas(Fenetre, width=500, height=500, bd=8)
zone_dessin.pack() #Affiche le Canvas 
zone_dessin.create_image(0, 0, anchor=tk.NW, image=map1)
zone_dessin.create_oval(150, 150, 350, 350, fill="orange", width=4) # On démarre la boucle Tkinter qui s'interrompt quand on ferme la fenêtre
Fenetre.mainloop()

class PremierRobot(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.map1 = tk.PhotoImage(file="fondcarte.png")
        self.zone_dessin = tk.Canvas(self, width=500, height=500, bd=8)
        self.zone_dessin.pack()
        self.zone_dessin.create_image(0, 0, anchor=tk.NW, image=self.map1)
        self.zone_dessin.create_oval(150, 150, 350, 350, fill="orange", width=4)
