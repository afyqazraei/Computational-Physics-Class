# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:58:44 2019

@author: afyqazraei
"""

import numpy as np
import matplotlib.pyplot as mp
    
def F(x):
    if x==1:
        return 0
    else:     
        return np.sin(x*np.pi)

def w(x,l,y):
    if l<0:
        return 1
    else:
        w=1
        for i in range(l+1):
            w*=(y-x[i])
        return w

def p(f,m,x,y):
    s=0
    for l in range(m):
        s+=f[l][0]*w(x,l-1,y)
    return s

print("this is Newton Interpolation for f(x)=sin pi*x")
m=int(input("enter number of nodes:"))
y=float(input("enter x:"))

x=[]

for i in range(m):
    a=float(input("enter node x:"))
    x.append(a)

f=[]
n=m

for j in range(m):
    f.append([])
    for k in range(n):
        if j==0:
            f[j].append(F(x[k]))
        else:
            f[j].append((f[j-1][k+1]-f[j-1][k])/(x[k+j]-x[k]))
    n-=1


print("f=", f)
s=p(f,m,x,y)
print("f(x)=", s)

g=np.arange(x[0],x[m-1],0.01)
h=len(g)
mp.plot(g,p(f,m,x,g))
mp.plot(y,s,'o')
mp.show()