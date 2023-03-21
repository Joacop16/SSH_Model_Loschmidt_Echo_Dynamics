#[Derivadas_2.f_0,Derivadas_2.f_1,Derivadas_2.f_2,Derivadas_2.f_3,Derivadas_2.f_4,Derivadas_2.f_5,Derivadas_2.f_6,Derivadas_2.f_7,Derivadas_2.f_8,Derivadas_2.f_9,Derivadas_2.f_10,Derivadas_2.f_11,Derivadas_2.f_12,Derivadas_2.f_13,Derivadas_2.f_14,Derivadas_2.f_15,Derivadas_2.f_16]

from Functions import f_0

def f_1(t, delta = 0.2):
    return (-f_0(t + 2*delta) + 8*f_0(t + delta) - 8*f_0(t - delta) + f_0(t - 2*delta))/(12*delta)

def f_2(t, delta = 0.2):
    return (-f_0(t + 2*delta) + 16*f_0(t + delta) - 30*f_0(t) + 16*f_0(t - delta) - f_0(t - 2*delta))/(12*delta**2)

def f_3(t, delta = 0.2):
    return (-f_0(t + 3*delta) + 8*f_0(t + 2*delta) - 13*f_0(t + delta) + 13*f_0(t - delta) - 8*f_0(t - 2*delta) + f_0(t - 3*delta))/(8*delta**3)

def f_4(t, delta = 0.2):
    return (-f_0(t + 3*delta) + 12*f_0(t + 2*delta) - 39*f_0(t + delta) + 56*f_0(t) - 39*f_0(t - delta) + 12*f_0(t - 2*delta) - f_0(t - 3*delta))/(6*delta**4)

def f_5(t, delta = 0.2):
    return (-f_4(t + 2*delta) + 8*f_4(t + delta) - 8*f_4(t - delta) + f_4(t - 2*delta))/(12*delta)

def f_6(t, delta = 0.2):
    return (-f_4(t + 2*delta) + 16*f_4(t + delta) - 30*f_4(t) + 16*f_4(t - delta) - f_4(t - 2*delta))/(12*delta**2)

def f_7(t, delta = 0.2):
    return (-f_4(t + 3*delta) + 8*f_4(t + 2*delta) - 13*f_4(t + delta) + 13*f_4(t - delta) - 8*f_4(t - 2*delta) + f_4(t - 3*delta))/(8*delta**3)

def f_8(t, delta = 0.2):
    return (-f_4(t + 3*delta) + 12*f_4(t + 2*delta) - 39*f_4(t + delta) + 56*f_4(t) - 39*f_4(t - delta) + 12*f_4(t - 2*delta) - f_4(t - 3*delta))/(6*delta**4)

def f_9(t, delta = 0.2):
    return (-f_8(t + 2*delta) + 8*f_8(t + delta) - 8*f_8(t - delta) + f_8(t - 2*delta))/(12*delta)

def f_10(t, delta = 0.2):
    return (-f_8(t + 2*delta) + 16*f_8(t + delta) - 30*f_8(t) + 16*f_8(t - delta) - f_8(t - 2*delta))/(12*delta**2)

def f_11(t, delta = 0.2):
    return (-f_8(t + 3*delta) + 8*f_8(t + 2*delta) - 13*f_8(t + delta) + 13*f_8(t - delta) - 8*f_8(t - 2*delta) + f_8(t - 3*delta))/(8*delta**3)

def f_12(t, delta = 0.2):
    return (-f_8(t + 3*delta) + 12*f_8(t + 2*delta) - 39*f_8(t + delta) + 56*f_8(t) - 39*f_8(t - delta) + 12*f_8(t - 2*delta) - f_8(t - 3*delta))/(6*delta**4)

def f_13(t, delta = 0.2):
    return (-f_12(t + 2*delta) + 8*f_12(t + delta) - 8*f_12(t - delta) + f_12(t - 2*delta))/(12*delta)

def f_14(t, delta = 0.2):
    return (-f_12(t + 2*delta) + 16*f_12(t + delta) - 30*f_12(t) + 16*f_12(t - delta) - f_12(t - 2*delta))/(12*delta**2)

def f_15(t, delta = 0.2):
    return (-f_12(t + 3*delta) + 8*f_12(t + 2*delta) - 13*f_12(t + delta) + 13*f_12(t - delta) - 8*f_12(t - 2*delta) + f_12(t - 3*delta))/(8*delta**3)

def f_16(t, delta = 0.2):
    return (-f_12(t + 3*delta) + 12*f_12(t + 2*delta) - 39*f_12(t + delta) + 56*f_12(t) - 39*f_12(t - delta) + 12*f_12(t - 2*delta) - f_12(t - 3*delta))/(6*delta**4)

