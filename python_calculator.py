import tkinter as tk
import math

class calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("400x500")
        self.root.resizable(0,0)

        self.entry = tk.Entry(self.root, font=("Arial", 20), justify="right")
        self.entry.pack(fill="both",padx=10, pady=10,)

    def click(self, value):
        self.entry.insert(tk.END, value)

    def clear(self):
        self.entry.delete(0, tk.END)

class advanced_calculator(calculator):

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def square_root(self):
        try:
            result = math.sqrt(float(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

   
    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

    def create_buttons(self):

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '√', '⌫']
        ]

        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")

            for btn in row:

                if btn == "=":
                    action = self.calculate
                elif btn == "C":
                    action = self.clear
                elif btn == "√":
                    action = self.square_root
                elif btn == "⌫":
                    action = self.backspace
                else:
                    action = lambda x=btn: self.click(x)

                tk.Button(
                    frame,
                    text=btn,
                    font=("Arial", 18),
                    command=action
                ).pack(side="left", expand=True, fill="both")


root = tk.Tk()

calc = advanced_calculator(root)
calc.create_buttons()

root.mainloop()