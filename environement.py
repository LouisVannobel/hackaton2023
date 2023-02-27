import tkinter as tk

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

if __name__ == '__main__':
    root = tk.Tk()
    tableau = Tableau(root)
    tableau.pack(side="top", fill="both", expand=True)
    root.mainloop()
