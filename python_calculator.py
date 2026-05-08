import tkinter as tk

root = tk.Tk()
root.title("python_calculator")
root.geometry("400x400")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

def click(value):
    entry.insert(tk.END, value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")