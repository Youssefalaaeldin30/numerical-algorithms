def lu(X11_r1, X12_r1, X13_r1, b1_r1, X21_r2, X22_r2, X23_r2, b2_r2, X31_r3, X32_r3, X33_r3, b3_r3, tree):
    # Calculate multipliers
    m21 = X21_r2 / X11_r1
    m31 = X31_r3 / X11_r1

    # Eliminate X1 from rows 2 and 3
    X21_r2 -= m21 * X11_r1
    X22_r2 -= m21 * X12_r1
    X23_r2 -= m21 * X13_r1
    
    X31_r3 -= m31 * X11_r1
    X32_r3 -= m31 * X12_r1
    X33_r3 -= m31 * X13_r1
   

    # Calculate multiplier for eliminating X2 from the third row
    m32 = X32_r3 / X22_r2

    # Eliminate X2 from the third row
    X32_r3 -= m32 * X22_r2
    X33_r3 -= m32 * X23_r2
    

    # Calculate solutions
    X11_l = 1
    X22_l = 1
    X33_l = 1
    X21_l = m21
    X31_l = m31
    X32_l = m32

    c1 = b1_r1 / X11_l
    c2 = (b2_r2 - X21_l * c1) / X22_l
    c3 = (b3_r3 - X31_l * c1 - X32_l * c2) / X33_l

    x3 = c3/X33_r3
    x2 = (c2 - X23_r2 * x3)/ X22_r2
    x1 = (c1 - X12_r1 * x2 - X13_r1 * x3)/X11_r1

    # Insert iteration data into the Treeview widget
    tree.insert("", "end", values=(x1, x2, x3))
