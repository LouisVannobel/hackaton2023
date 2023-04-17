import tkinter as tk
from agents.environnement.carte import Tableau, BorneRecharge
from agents.environnement.base import Base
from agents.environnement.Premier_Robot import Fenetre
from agents.robot import Robot, Equipe
from agents.object import Objet

def main():
    root = tk.Tk()

    # Créer et configurer la carte
    bornes_recharge = [BorneRecharge(5, 5), BorneRecharge(15, 10)]
    tableau = Tableau(root, bornes_recharge=bornes_recharge)
    tableau.pack(side="top", fill="both", expand=True)

    # Créer et configurer la base
    base = Base(row=0, column=0)

    # Créez et configurez vos objets
    objets = [Objet("Pomme", 5, 1, tableau), Objet("Banane", 3, 2, tableau), Objet("Orange", 4, 3, tableau)]

    # Créer et configurer les équipes et robots
    equipe1 = Equipe(1)
    equipe2 = Equipe(2)

    robot1 = Robot("Robot1", 2, 3, tableau, equipe=equipe1)
    robot2 = Robot("Robot2", 3, 2, tableau, equipe=equipe2)

    equipe1.ajouter_robot(robot1)
    equipe2.ajouter_robot(robot2)

    def update_simulation():
        for robot in [robot1, robot2]:
            for objet in objets:
                if objet in robot.detecter_objet(objets):
                    robot.se_deplacer_vers_objet(objet, base)
                    tableau.mise_a_jour(robot.row, robot.column, "R", "blue")
                    tableau.mise_a_jour(objet.row, objet.column, "O", "yellow")
                else:
                    tableau.move(robot.row, robot.column)
                    tableau.mise_a_jour(robot.row, robot.column, "R", "blue")
        root.after(100, update_simulation)


    update_simulation()
    root.mainloop()

if __name__ == "__main__":
    main()
