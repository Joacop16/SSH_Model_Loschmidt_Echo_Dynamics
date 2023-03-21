#[Recurrencias.D_0,Recurrencias.D_1,Recurrencias.D_2,Recurrencias.D_3,Recurrencias.D_4,Recurrencias.D_5,Recurrencias.D_6,Recurrencias.D_7,Recurrencias.D_8,Recurrencias.D_9,Recurrencias.D_10,Recurrencias.D_11,Recurrencias.D_12,Recurrencias.D_13,Recurrencias.D_14]

from Functions import D_0
from Functions import a_coefs
from Functions import b_coefs
from scipy.misc import derivative

def D_1(t):
    D_Kprima = derivative(D_0, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_0(t)*a_coefs[0])/b_coefs[1]

def D_2(t):
    D_Kprima = derivative(D_1, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_1(t)*a_coefs[1] - b_coefs[1]*D_0(t))/b_coefs[2]

def D_3(t):
    D_Kprima = derivative(D_2, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_2(t)*a_coefs[2] - b_coefs[2]*D_1(t))/b_coefs[3]

def D_4(t):
    D_Kprima = derivative(D_3, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_3(t)*a_coefs[3] - b_coefs[3]*D_2(t))/b_coefs[4]

def D_5(t):
    D_Kprima = derivative(D_4, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_4(t)*a_coefs[4] - b_coefs[4]*D_3(t))/b_coefs[5]

def D_6(t):
    D_Kprima = derivative(D_5, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_5(t)*a_coefs[5] - b_coefs[5]*D_4(t))/b_coefs[6]

def D_7(t):
    D_Kprima = derivative(D_6, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_6(t)*a_coefs[6] - b_coefs[6]*D_5(t))/b_coefs[7]

def D_8(t):
    D_Kprima = derivative(D_7, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_7(t)*a_coefs[7] - b_coefs[7]*D_6(t))/b_coefs[8]

def D_9(t):
    D_Kprima = derivative(D_8, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_8(t)*a_coefs[8] - b_coefs[8]*D_7(t))/b_coefs[9]

def D_10(t):
    D_Kprima = derivative(D_9, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_9(t)*a_coefs[9] - b_coefs[9]*D_8(t))/b_coefs[10]

def D_11(t):
    D_Kprima = derivative(D_10, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_10(t)*a_coefs[10] - b_coefs[10]*D_9(t))/b_coefs[11]

def D_12(t):
    D_Kprima = derivative(D_11, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_11(t)*a_coefs[11] - b_coefs[11]*D_10(t))/b_coefs[12]

def D_13(t):
    D_Kprima = derivative(D_12, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_12(t)*a_coefs[12] - b_coefs[12]*D_11(t))/b_coefs[13]

def D_14(t):
    D_Kprima = derivative(D_13, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_13(t)*a_coefs[13] - b_coefs[13]*D_12(t))/b_coefs[14]

def D_15(t):
    D_Kprima = derivative(D_14, x0 = t, dx= 0.3, n = 1 , order = 7)
    return (1j*D_Kprima - D_14(t)*a_coefs[14] - b_coefs[14]*D_13(t))/b_coefs[15]

