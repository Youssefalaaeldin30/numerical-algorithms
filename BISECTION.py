import math

def f(x, func):
    return eval(func)

def BISECTION(func, Xl, Xu, eps, tree):
    error = float('inf')  # Initialize error to a large value
    Xr = 0
    Xrold = 0
    iter = 0

    while error > eps:
        Xrold = Xr
        Xr = (Xl + Xu) / 2
        if iter != 0:
            error = abs((Xr - Xrold) / Xr) * 100

        # Format the values with three decimal places
        Xl_formatted = "{:.3f}".format(Xl)
        Xu_formatted = "{:.3f}".format(Xu)
        Xr_formatted = "{:.3f}".format(Xr)
        error_formatted = "{:.3f}".format(error)
        f_Xl_formatted = "{:.3f}".format(f(Xl, func))
        f_Xu_formatted = "{:.3f}".format(f(Xu, func))
        f_Xr_formatted = "{:.3f}".format(f(Xr, func))

        # Insert iteration data into the Treeview widget
        tree.insert("", "end", text=str(iter), values=(Xl_formatted, f_Xl_formatted, Xu_formatted, f_Xu_formatted, 
                                                        Xr_formatted, f_Xr_formatted, error_formatted))


        if f(Xl, func) * f(Xr, func) > 0:
            Xl = Xr
        else:
            Xu = Xr

        iter += 1



    return Xr
