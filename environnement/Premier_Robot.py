
# On importe Tkinter 
from tkinter import *  # On cree une fenetre, racine de notre interface 
Fenetre = Tk()  # Dans Fenetre nous allons creer un objet type Canvas qui se nomme zone_dessin # Nous donnons des valeurs aux proprietes "width", "height", "bg", "bd" 
zone_dessin = Canvas(Fenetre,width=500,height=500,bg="white",bd=8) 
zone_dessin.pack() #Affiche le Canvas  
zone_dessin.create_oval(150,150,350,350,fill="orange",width=4)    # On demarre la boucle Tkinter qui s'interompt quand on ferme la fenetre 
Fenetre.mainloop()