def Gauss_jordan(X11_r1, X12_r1, X13_r1, b1_r1, X21_r2, X22_r2, X23_r2, b2_r2, X31_r3, X32_r3, X33_r3, b3_r3,tree):




    
    m21 = X21_r2 / X11_r1
    m31 = X31_r3 / X11_r1

    X21_r2 -= m21 * X11_r1
    X22_r2 -= m21 * X12_r1
    X23_r2 -= m21 * X13_r1
    b2_r2 -= m21 * b1_r1

    X31_r3 -= m31 * X11_r1
    X32_r3 -= m31 * X12_r1
    X33_r3 -= m31 * X13_r1
    b3_r3 -= m31 * b1_r1

    m32 = X32_r3 / X22_r2
    X32_r3 -= m32 * X22_r2
    X33_r3 -= m32 * X23_r2
    b3_r3 -= m32 * b2_r2

    x3 = b3_r3 / X33_r3
    x2 = (b2_r2 - X23_r2 * x3) / X22_r2
    x1 = (b1_r1 - X12_r1 * x2 - X13_r1 * x3) / X11_r1
    tree.insert("", "end", values=(x1, x2, x3))