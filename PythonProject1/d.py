from math import *


a = int(input())
def z1(a):
    x = cos(a) + sin(a) + cos(3*a) + sin(3*a)
    return x

def z2(a):
    y = 1/4 - 1/4*sin(5/2*pi - 8*a)
    return y


print(round(z1(a),3))
print(round(z2(a),3))