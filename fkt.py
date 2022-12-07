# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:02:14 2022

@author: tim
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Extrema Suche für Funktion
# =============================================================================
def Extrema(Funktion, Bereich, Art=0):
    """
    Gibt die numerische Maxima/Minima x-stelle, sowie den y-wert

    Funktion : Die Funktion für bsp f(x) muss hier f eingegeben werden

    Bereich : x- Bereich bsp als variable eines linspace

    Art : Maxima (0), Mimima (1)

    Returns (x-stelle, y-wert)

    """
    def f_intern(x):
        f_intern = Funktion(x)
        return f_intern

    if Art == 0:
        wert= -1e100
        stelle= "error in Maxima findung"

        for i in Bereich:
            if f_intern(i) >= wert:
                wert = f_intern(i)
                stelle = i


            elif f_intern(i) <= wert:
                break

    elif Art == 1:
        wert= 1e100
        stelle= "error in Minima findung"

        for i in Bereich:
            if f_intern(i) <= wert:
                wert = f_intern(i)
                stelle = i

            elif f_intern(i) >= wert:
                break

    return(stelle,wert)



# =============================================================================
# Plot einer Regressionskurve als plt.plot
# =============================================================================
def y_regression(x,y, Grad = 1, Plot=True):
    """
    Regression vom Grad n
    x und y sind np.array
    Grad ist n=1,2,3,4,5...

    Returns np.array mit y werten

    """
    y_reg_grad = 0

    max_val = np.max(x)
    min_val = np.min(x)
    x_sp = np.linspace(min_val, max_val, 1000)


    pol1 = np.polyfit(x, y, Grad)
    pol = np.flip(pol1)

    for i in range(0, Grad):
        y_reg_grad = y_reg_grad +  pol[i] * x_sp **(i)


    y2 = y_reg_grad

    if Plot == True:
        plt.plot(x_sp,y2)

    return y2

# =============================================================================
# Lineare Regression für Lineare Steigungn, y-fehler basiert
# =============================================================================
def linear_reg(x , y , y_err):
    x_ges = np.append(np.append(x,x),x) # 3 mal die x daten hintereinander
    y_ges = np.append(np.append(y + y_err , y - y_err),y) # Reihung von y-werten, max und min fehler werten
    m,b = np.polyfit(x_ges, y_ges, 1)
    y_Reg_lin = m * x_ges +b
    R2 = 1-((np.sum((y_ges - y_Reg_lin)**2))/(np.sum((y_ges - np.mean(y_ges))**2)))
    dm = (m - m*R2)

    print("Lineare Regression")
    print("m=",m)
    print("b=",b)
    print("R2=",R2)
    print("dm=",dm)
    print()

"""
lin_reg_var = bool(True) # bool True/False
if lin_reg_var == True:
    x_ges = np.append(np.append(x_data,x_data),x_data) # 3 mal die x daten hintereinander
    y_ges = np.append(np.append(y_data + y_err , y_data - y_err),y_data) # Reihung von y-werten, max und min fehler werten
    m,b = np.polyfit(x_ges, y_ges, 1)
    y_Reg_lin = m * x_ges +b
    R2 = 1-((np.sum((y_ges - y_Reg_lin)**2))/(np.sum((y_ges - np.mean(y_ges))**2)))
    dm = (m - m*R2)

    print("Lineare Regression von",Name_Excel)
    print("m=",m)
    print("b=",b)
    print("R2=",R2)
    print("dm=",dm)
    print()
"""
