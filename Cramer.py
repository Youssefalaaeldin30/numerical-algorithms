def Cramer(X11_r1, X12_r1, X13_r1, b1_r1, X21_r2, X22_r2, X23_r2, b2_r2, X31_r3, X32_r3, X33_r3, b3_r3,tree):
    

    a=X11_r1*(X22_r2 *X33_r3 - X23_r2 * X32_r3 ) - X12_r1*(X21_r2*X33_r3 - X31_r3 * X23_r2) + X13_r1 * (X21_r2*X32_r3 - X31_r3 * X22_r2)
    a1=b1_r1*(X22_r2 *X33_r3 - X23_r2 * X32_r3 ) - X12_r1*(b2_r2*X33_r3 - b3_r3 * X23_r2) + X13_r1 * (b2_r2*X32_r3 - b3_r3 * X22_r2)
    a2=X11_r1*(b2_r2 *X33_r3 - X23_r2 * b3_r3 ) - b1_r1*(X21_r2*X33_r3 - X31_r3 * X23_r2) + X13_r1 * (X21_r2*b3_r3 - X31_r3 * b2_r2)
    a3=X11_r1*(X22_r2 *b3_r3 - b2_r2 * X32_r3 ) - X12_r1*(X21_r2*b3_r3 - X31_r3 * b2_r2) + b1_r1 * (X21_r2*X32_r3 - X31_r3 * X22_r2)


    x1= a1/a
    x2= a2/a
    x3= a3/a
    # Insert iteration data into the Treeview widget
    tree.insert("", "end", values=(x1, x2, x3))
