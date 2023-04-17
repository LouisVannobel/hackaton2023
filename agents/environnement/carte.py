import tkinter as tk

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
                
        for borne in self.bornes_recharge:
            self.cell[borne.row, borne.column].config(bg="green")
            
    def mise_a_jour(self, row, column, text, color):
        self.cell[row, column].config(fg=color)
        self.cell[row, column].delete(0, "end")
        self.cell[row, column].insert(0, text)


if __name__ == '__main__':
    root = tk.Tk()
    bornes_recharge = [BorneRecharge(5, 5), BorneRecharge(15, 10)]
    tableau = Tableau(root, bornes_recharge=bornes_recharge)
    tableau.pack(side="top", fill="both", expand=True)
    root.mainloop()
