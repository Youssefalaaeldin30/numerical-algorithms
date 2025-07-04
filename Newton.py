import math

error = float('inf')  # Initialize error to a large value
iter = 0

def f(x, func):
    return eval(func)



def df( x,func):
    h=0.0001
    return (f(x + h, func) - f(x, func)) / h
'''
def df(x, derivfunc):
    return eval(derivfunc)
'''


def newton(func, Xi, eps, tree):
    global iter, error

    i = Xi - (f(Xi, func) / df(Xi, func))

    # Format the values with three decimal places
    Xi_formatted = "{:.3f}".format(Xi)
    error_formatted = "{:.3f}".format(error)
    f_Xi_formatted = "{:.3f}".format(f(Xi, func))
    df_Xi_formatted = "{:.3f}".format(df(Xi, func))

    # Insert iteration data into the Treeview widget
    tree.insert("", "end", text=str(iter), values=(Xi_formatted, f_Xi_formatted, df_Xi_formatted, error_formatted))

    if error > eps:
        iter += 1
        if iter != 0:
            error = abs((i - Xi) / i) * 100
        Xi = i
        newton(func, Xi, eps, tree)
    return Xi
