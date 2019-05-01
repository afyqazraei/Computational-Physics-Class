# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:56:57 2019

@author: afyqazraei
"""

import numpy as np
import matplotlib.pyplot as mp
    
def F(x):
    return np.sin(np.pi*x)

def L(x,m,y,j):
    l=1
    for i in range(m):
        if i==j:
            l*=1
        else:
            l*=(y-x[i])/(x[j]-x[i])     
    return l

def p(f,m,x,y):
    s=0
    for l in range(m):
        s=s+f[l]*L(x,m,y,l)
    return s

print("this is Lagrange Interpolation for f(x)=sin pi*x")
m=int(input("enter number of nodes:"))
y=float(input("enter x:"))

x=[]

for i in range(m):
    a=float(input("enter node x:"))
    x.append(a)

f=[]

for j in range(m):
    f.append(F(x[j]))

print("f=", f)
s=p(f,m,x,y)
print("f(x)=", s)

g=np.arange(x[0],x[m-1],0.01)
h=len(g)
mp.plot(g,p(f,m,x,g))
mp.plot(y,s,'o')
mp.show()