import math
error = float('inf')  # Initialize error to a large value
iter = 0
def f(x,func):
        return eval(func)

def Secant(func, xi_minus1, Xi, eps,tree ):

    global iter, error
    
    
    
    # Format the values with three decimal places
    Xi_formatted = "{:.3f}".format(Xi)
    error_formatted = "{:.3f}".format(error)
    f_Xi_formatted = "{:.3f}".format(f(Xi, func))
    Xi_minus1_formatted="{:.3f}".format(xi_minus1)
    f_Xi_minus1_formatted = "{:.3f}".format(f(xi_minus1,func))

    # Insert iteration data into the Treeview widget
    tree.insert("", "end", text=str(iter), values=(Xi_minus1_formatted,f_Xi_minus1_formatted,Xi_formatted, f_Xi_formatted,  error_formatted))
    x1 = xi_minus1 - (f(xi_minus1,func) * (Xi - xi_minus1) / (f(Xi,func) - f(xi_minus1,func)))
    xi_minus1 = Xi
    if error > eps:
        iter += 1
        if iter != 0:
            error = abs((Xi - xi_minus1) / Xi) * 100
        Xi = x1
        Secant(func, xi_minus1, Xi, eps,tree)

    return Xi
    
    
    
