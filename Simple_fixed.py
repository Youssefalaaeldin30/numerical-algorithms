import math

error = float('inf')  # Initialize error to a large value
iter = 0

def f(x, func):
    return eval(func)

def Fixed_point(func, Xi, eps, tree):
    global iter, error

    Xi_plus1 = f(Xi, func)
    
    # Format the values with three decimal places
    Xi_formatted = "{:.3f}".format(Xi)
    error_formatted = "{:.3f}".format(error)
    f_Xi_formatted = "{:.3f}".format(f(Xi, func))

    # Insert iteration data into the Treeview widget
    tree.insert("", "end", text=str(iter), values=(Xi_formatted, f_Xi_formatted, error_formatted))
    
    if error > eps:
        iter += 1
        if iter != 0:
            error = abs((Xi_plus1 - Xi) / Xi_plus1) * 100
        Fixed_point(func, Xi_plus1, eps, tree)

    return Xi_plus1
