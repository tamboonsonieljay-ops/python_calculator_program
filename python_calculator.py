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

def clear():
    entry.delete(0, tk.END)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            action = calculate
        elif btn == "C":
            action = clear
        else:
            action = lambda x=btn: click(x)

        tk.Button(
            frame,
            text=btn,
            font=("Arial", 18),
            command=action
        ).pack(side="left", expand=True, fill="both")

root.mainloop()