import numpy as np

def first_bdry(x,y):
    return x**2 + y**2

def second_bdry(x,y):
    return 12

def third_bdry(x,y):
    return x**2 - y**2

def forth_bdry(x,y):
    return x * np.sin(2*y)

def fifth_bdry(x,y):
    return x**3 - 4*y

def sixth_bdry(x,y):
    return np.cos(x*y)

def seventh_bdry(x,y):
    return y

bdry_funcs = [first_bdry,second_bdry,third_bdry,forth_bdry,fifth_bdry,sixth_bdry,seventh_bdry]

#print(bdry_funcs[0](1,1))