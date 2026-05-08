import tkinter as tk

root = tk.Tk()
root.title("python_calculator")
root.geometry("400x400")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)