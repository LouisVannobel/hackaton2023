import tkinter as tk
import random

class BorneRecharge:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Tableau(tk.Frame):
    def __init__(self, parent, rows=30, columns=30, bornes_recharge=[]):
        tk.Frame.__init__(self, parent)
        self.rows = rows
        self.columns = columns
        self.bornes_recharge = bornes_recharge
        self.cell = {}
        
        for row in range(self.rows):
            for column in range(self.columns):
                self.cell[row, column] = tk.Entry(self, width=3)
                self.cell[row, column].grid(row=row, column=column)
                
        self.place_random_bornes_recharge()
        
    def place_random_bornes_recharge(self):
        indices = random.sample(range(self.rows * self.columns), len(self.bornes_recharge))
        for i, borne in enumerate(self.bornes_recharge):
            row = indices[i] // self.columns
            column = indices[i] % self.columns
            borne.row = row
            borne.column = column
            self.cell[row, column].config(bg="green")
            
    def mise_a_jour(self, row, column, text, color):
        self.cell[row, column].config(fg=color)
        self.cell[row, column].delete(0, "end")
        self.cell[row, column].insert(0, text)


if __name__ == '__main__':
    root = tk.Tk()
    bornes_recharge = [BorneRecharge(0, 0), BorneRecharge(0, 0)]  # Placeholder values for rows and columns
    tableau = Tableau(root, bornes_recharge=bornes_recharge)
    tableau.pack(side="top", fill="both", expand=True)
    root.mainloop()
