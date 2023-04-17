import tkinter as tk
import random

class Tableau(tk.Frame):
    def __init__(self, parent, rows=30, columns=30):
        tk.Frame.__init__(self, parent)
        self.rows = rows
        self.columns = columns
        self.cell = {}
        for row in range(self.rows):
            for column in range(self.columns):
                self.cell[row, column] = tk.Entry(self, width=3)
                self.cell[row, column].grid(row=row, column=column)

    def move(self, row, column):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        direction = random.choice(directions)
        new_row = row + direction[0]
        new_column = column + direction[1]
        if new_row < 0 or new_row >= self.rows or new_column < 0 or new_column >= self.columns:
            return row, column
        self.cell[row, column].delete(0, tk.END)
        self.cell[new_row, new_column].insert(0, "X")
        return new_row, new_column
    
    def position_aleatoire_objet(self):
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        return row, column
    
    def mise_a_jour(self, row, column, text, color="white"):
        self.cell[row, column].delete(0, tk.END)
        self.cell[row, column].insert(0, text)
        self.cell[row, column].config(bg=color)



if __name__ == '__main__':
    root = tk.Tk()
    tableau = Tableau(root)
    tableau.pack(side="top", fill="both", expand=True)

    # Initial position of the object
    current_row, current_column = tableau.position_aleatoire_objet()
    tableau.cell[current_row, current_column].insert(0, "X")

    root.mainloop()
