import math
import tkinter as tk
from tkinter import ttk
import customtkinter

# Numerical Methods Imports
from BISECTION import BISECTION
from False_position import False_postion
from Simple_fixed import Fixed_point
from Newton import newton
from Secant import Secant
from Gauss_elimination import ge
from LU_decomposition import lu
from Cramer import Cramer
from Gauss_jordan import Gauss_jordan

# App Configuration
customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Numerical Methods Solver")
app.geometry("1100x900")

tabview = customtkinter.CTkTabview(app, width=1400, height=800)
methods = [
    "Bisection", "The False Position", "Simple Fixed Point",
    "Newton", "Secant", "Gauss Elimination",
    "LU Decomposition", "Cramer", "Gauss_gordan"
]
for method in methods:
    tabview.add(method)
tabview.set("Bisection")
tabview.pack()

customtkinter.CTkLabel(app, text="Choose the method you want to solve with:").pack()

# Helper Functions

def create_treeview(tab_name, columns):
    tree = ttk.Treeview(tabview.tab(tab_name))
    tree["columns"] = columns
    tree.heading("#0", text="i")
    for col in columns:
        tree.heading(col, text=col)
    tree.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    return tree

def create_input(tab_name, fields, start_y=0.05):
    entries = {}
    for i, (label_text, placeholder) in enumerate(fields):
        rel_y = start_y + i * 0.05
        label = customtkinter.CTkLabel(tabview.tab(tab_name), text=label_text)
        label.place(relx=0.2, rely=rel_y, anchor=tk.CENTER)
        entry = customtkinter.CTkEntry(tabview.tab(tab_name), placeholder_text=placeholder, width=250, height=30)
        entry.place(relx=0.5, rely=rel_y, anchor=tk.CENTER)
        entries[placeholder] = entry
    return entries

# Button Function Generator

def add_solver_button(tab_name, command, rely=0.25):
    customtkinter.CTkButton(
        tabview.tab(tab_name), text="Solve", fg_color="green", command=command
    ).place(relx=0.5, rely=rely, anchor=tk.CENTER)

# Bisection
bi_entries = create_input("Bisection", [
    ("Enter Equation", "Equation"),
    ("Enter Xl", "Xl"),
    ("Enter Xu", "Xu"),
    ("Enter Error", "Error")
])
def solve_bisection():
    func = bi_entries["Equation"].get()
    Xl = float(bi_entries["Xl"].get())
    Xu = float(bi_entries["Xu"].get())
    eps = float(bi_entries["Error"].get())
    tree = create_treeview("Bisection", ["Xl", "f(Xl)", "Xu", "f(Xu)", "Xr", "f(Xr)", "error"])
    BISECTION(func, Xl, Xu, eps, tree)
add_solver_button("Bisection", solve_bisection)

# False Position
fp_entries = create_input("The False Position", [
    ("Enter Equation", "Equation"),
    ("Enter Xl", "Xl"),
    ("Enter Xu", "Xu"),
    ("Enter Error", "Error")
])
def solve_false_position():
    func = fp_entries["Equation"].get()
    Xl = float(fp_entries["Xl"].get())
    Xu = float(fp_entries["Xu"].get())
    eps = float(fp_entries["Error"].get())
    tree = create_treeview("The False Position", ["Xl", "f(Xl)", "Xu", "f(Xu)", "Xr", "f(Xr)", "error"])
    False_postion(func, Xl, Xu, eps, tree)
add_solver_button("The False Position", solve_false_position)

# Fixed Point
fp_entries = create_input("Simple Fixed Point", [
    ("Enter Equation", "Equation"),
    ("Enter Xi", "Xi"),
    ("Enter Error", "Error")
])
def solve_fixed_point():
    func = fp_entries["Equation"].get()
    Xi = float(fp_entries["Xi"].get())
    eps = float(fp_entries["Error"].get())
    tree = create_treeview("Simple Fixed Point", ["Xi", "f(Xi)", "error"])
    Fixed_point(func, Xi, eps, tree)
add_solver_button("Simple Fixed Point", solve_fixed_point)

# Newton
ne_entries = create_input("Newton", [
    ("Enter Equation", "Equation"),
    ("Enter Xi", "Xi"),
    ("Enter Error", "Error")
])
def solve_newton():
    func = ne_entries["Equation"].get()
    Xi = float(ne_entries["Xi"].get())
    eps = float(ne_entries["Error"].get())
    tree = create_treeview("Newton", ["Xi", "f(Xi)", "df(Xi)", "error"])
    newton(func, Xi, eps, tree)
add_solver_button("Newton", solve_newton)

# Secant
sec_entries = create_input("Secant", [
    ("Enter Equation", "Equation"),
    ("Enter Xi-1", "Xi-1"),
    ("Enter Xi", "Xi"),
    ("Enter Error", "Error")
])
def solve_secant():
    func = sec_entries["Equation"].get()
    Xi_1 = float(sec_entries["Xi-1"].get())
    Xi = float(sec_entries["Xi"].get())
    eps = float(sec_entries["Error"].get())
    tree = create_treeview("Secant", ["Xi-1", "f(Xi-1)", "Xi", "f(Xi)", "error"])
    Secant(func, Xi_1, Xi, eps, tree)
add_solver_button("Secant", solve_secant)

# Systems Solvers Template

def create_system_input(tab_name):
    labels = ["X1", "X2", "X3", "B"]
    positions = [0.35, 0.45, 0.55, 0.65]
    entries = []
    for row in range(3):
        for i, (label, x_pos) in enumerate(zip(labels, positions)):
            if row == 0:
                customtkinter.CTkLabel(tabview.tab(tab_name), text=f"Enter {label}").place(relx=x_pos, rely=0.04, anchor=tk.CENTER)
            e = customtkinter.CTkEntry(tabview.tab(tab_name), placeholder_text=f"{label.lower()}{row+1}", width=100, height=30)
            e.place(relx=positions[i], rely=0.08 + 0.05 * row, anchor=tk.CENTER)
            entries.append(e)
    return entries

def parse_system_entries(entries):
    return [float(e.get()) for e in entries]

# Gauss Elimination
ge_entries = create_system_input("Gauss Elimination")
def solve_gauss_elimination():
    values = parse_system_entries(ge_entries)
    tree = create_treeview("Gauss Elimination", ["x1", "x2", "x3"])
    ge(*values, tree)
add_solver_button("Gauss Elimination", solve_gauss_elimination, 0.23)

# LU Decomposition
lu_entries = create_system_input("LU Decomposition")
def solve_lu():
    values = parse_system_entries(lu_entries)
    tree = create_treeview("LU Decomposition", ["x1", "x2", "x3"])
    lu(*values, tree)
add_solver_button("LU Decomposition", solve_lu, 0.23)

# Cramer
cr_entries = create_system_input("Cramer")
def solve_cramer():
    values = parse_system_entries(cr_entries)
    tree = create_treeview("Cramer", ["x1", "x2", "x3"])
    Cramer(*values, tree)
add_solver_button("Cramer", solve_cramer, 0.23)

# Gauss Jordan
gj_entries = create_system_input("Gauss_gordan")
def solve_gauss_jordan():
    values = parse_system_entries(gj_entries)
    tree = create_treeview("Gauss_gordan", ["x1", "x2", "x3"])
    Gauss_jordan(*values, tree)
add_solver_button("Gauss_gordan", solve_gauss_jordan, 0.23)

app.mainloop()