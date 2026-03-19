import tkinter as tk
import math

# ---------- Logic ----------
def safe_eval(expr):
    try:
        return eval(expr, {"__builtins__": None}, {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10
        })
    except:
        return "Error"

def press(val):
    display_var.set(display_var.get() + str(val))

def clear():
    display_var.set("")

def backspace():
    display_var.set(display_var.get()[:-1])

def calculate():
    expr = display_var.get()
    result = safe_eval(expr)
    display_var.set(result)

# ---------- UI ----------
root = tk.Tk()
root.title("Calculator")
root.geometry("350x520")
root.configure(bg="#1f2937")

# 🔥 macOS Focus Fix
root.lift()
root.attributes('-topmost', True)
root.after(200, lambda: root.attributes('-topmost', False))
root.after(100, lambda: root.focus_force())

display_var = tk.StringVar()

# Display
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 26),
    bg="#111827",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
display.pack(fill="both", padx=12, pady=15, ipady=18)

# Frame
frame = tk.Frame(root, bg="#1f2937")
frame.pack()

# Button Creator
def create_btn(text, r, c, cmd, color="#374151"):
    btn = tk.Button(
        frame,
        text=text,
        command=cmd,
        font=("Arial", 14, "bold"),
        width=5,
        height=2,
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        bd=0,
        relief="flat"
    )
    btn.grid(row=r, column=c, padx=6, pady=6)

# Buttons Layout
buttons = [
    ["C", "⌫", "(", ")"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == "=":
            create_btn(char, i, j, calculate, "#10b981")  # green
        elif char == "C":
            create_btn(char, i, j, clear, "#ef4444")  # red
        elif char == "⌫":
            create_btn(char, i, j, backspace, "#f59e0b")  # orange
        else:
            create_btn(char, i, j, lambda x=char: press(x))

# Scientific Buttons
create_btn("sin", 5, 0, lambda: press("sin("), "#2563eb")
create_btn("cos", 5, 1, lambda: press("cos("), "#2563eb")
create_btn("tan", 5, 2, lambda: press("tan("), "#2563eb")
create_btn("√", 5, 3, lambda: press("sqrt("), "#2563eb")
create_btn("log", 6, 0, lambda: press("log("), "#059669")

root.mainloop()