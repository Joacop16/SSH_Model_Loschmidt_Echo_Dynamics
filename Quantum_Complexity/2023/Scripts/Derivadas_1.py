#[Derivadas_1.f_0,Derivadas_1.f_1,Derivadas_1.f_2,Derivadas_1.f_3,Derivadas_1.f_4,Derivadas_1.f_5,Derivadas_1.f_6,Derivadas_1.f_7,Derivadas_1.f_8,Derivadas_1.f_9,Derivadas_1.f_10,Derivadas_1.f_11,Derivadas_1.f_12,Derivadas_1.f_13,Derivadas_1.f_14]

from Functions import f_0

def f_1(t, delta = 0.2):
    return (f_0(t + delta) - f_0(t - delta))/(2*delta)

def f_2(t, delta = 0.2):
    return (f_1(t + delta) - f_1(t - delta))/(2*delta)

def f_3(t, delta = 0.2):
    return (f_2(t + delta) - f_2(t - delta))/(2*delta)

def f_4(t, delta = 0.2):
    return (f_3(t + delta) - f_3(t - delta))/(2*delta)

def f_5(t, delta = 0.2):
    return (f_4(t + delta) - f_4(t - delta))/(2*delta)

def f_6(t, delta = 0.2):
    return (f_5(t + delta) - f_5(t - delta))/(2*delta)

def f_7(t, delta = 0.2):
    return (f_6(t + delta) - f_6(t - delta))/(2*delta)

def f_8(t, delta = 0.2):
    return (f_7(t + delta) - f_7(t - delta))/(2*delta)

def f_9(t, delta = 0.2):
    return (f_8(t + delta) - f_8(t - delta))/(2*delta)

def f_10(t, delta = 0.2):
    return (f_9(t + delta) - f_9(t - delta))/(2*delta)

def f_11(t, delta = 0.2):
    return (f_10(t + delta) - f_10(t - delta))/(2*delta)

def f_12(t, delta = 0.2):
    return (f_11(t + delta) - f_11(t - delta))/(2*delta)

def f_13(t, delta = 0.2):
    return (f_12(t + delta) - f_12(t - delta))/(2*delta)

def f_14(t, delta = 0.2):
    return (f_13(t + delta) - f_13(t - delta))/(2*delta)

