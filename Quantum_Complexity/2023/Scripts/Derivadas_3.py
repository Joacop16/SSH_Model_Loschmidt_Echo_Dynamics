#[Derivadas_3.f_0,Derivadas_3.f_1,Derivadas_3.f_2,Derivadas_3.f_3,Derivadas_3.f_4,Derivadas_3.f_5,Derivadas_3.f_6,Derivadas_3.f_7,Derivadas_3.f_8,Derivadas_3.f_9,Derivadas_3.f_10,Derivadas_3.f_11,Derivadas_3.f_12,Derivadas_3.f_13,Derivadas_3.f_14]

from Functions import f_0
from scipy.misc import derivative

def f_1(t, delta = 0.3):
    return derivative(f_0, x0 = t, dx= delta, n = 1 , order = 7)

def f_2(t, delta = 0.3):
    return derivative(f_1, x0 = t, dx= delta, n = 1 , order = 7)

def f_3(t, delta = 0.3):
    return derivative(f_2, x0 = t, dx= delta, n = 1 , order = 7)

def f_4(t, delta = 0.3):
    return derivative(f_3, x0 = t, dx= delta, n = 1 , order = 7)

def f_5(t, delta = 0.3):
    return derivative(f_4, x0 = t, dx= delta, n = 1 , order = 7)

def f_6(t, delta = 0.3):
    return derivative(f_5, x0 = t, dx= delta, n = 1 , order = 7)

def f_7(t, delta = 0.3):
    return derivative(f_6, x0 = t, dx= delta, n = 1 , order = 7)

def f_8(t, delta = 0.3):
    return derivative(f_7, x0 = t, dx= delta, n = 1 , order = 7)

def f_9(t, delta = 0.3):
    return derivative(f_8, x0 = t, dx= delta, n = 1 , order = 7)

def f_10(t, delta = 0.3):
    return derivative(f_9, x0 = t, dx= delta, n = 1 , order = 7)

def f_11(t, delta = 0.3):
    return derivative(f_10, x0 = t, dx= delta, n = 1 , order = 7)

def f_12(t, delta = 0.3):
    return derivative(f_11, x0 = t, dx= delta, n = 1 , order = 7)

def f_13(t, delta = 0.3):
    return derivative(f_12, x0 = t, dx= delta, n = 1 , order = 7)

def f_14(t, delta = 0.3):
    return derivative(f_13, x0 = t, dx= delta, n = 1 , order = 7)

