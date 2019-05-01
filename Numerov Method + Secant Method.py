# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:10:29 2019

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as mpl


def g(x):
    return -4

def s(x):
    return -4*x

def f(x,y,n):
    return (2*y[n]*(1-5*(h**3)*g(x[n])/12)-y[n-1]*(1+(h**2)*g(x[n-1])/12)+(h**2)*(s(x[n+1])+10*s(x[n])+s(x[n-1])))/(1+(h**2)*g(x[n+1])/12)

xi=0
xf=1   
ui=0
uf=2
ur=[]
N=10
h=(xf-xi)/N
tol=10**(-5)

x=np.arange(xi,xf+h,h)
print("x=", x)
print("")
u1=[]
m=(uf-ui)/(xf-xi)
z=m*x[1]+ui
u1.append(z)

k=0
i=0


while k==0:
    j=0
    u=[]
    n=2
    u.append(ui)
    u.append(u1[i])
    
    while j==0:     
        un=f(x,u,n-1)
        u.append(un)
        print("u=", u)
        if len(u)==len(x):
            j+=1
        n+=1
    ur.append(u)
    mpl.plot(x,u)
    print("")
    
        
    if len(u1)>1:
        z=u1[i-1]+(u1[i]-u1[i-1])*(uf-ur[i-1][N])/(ur[i][N]-ur[i-1][N])
        u1.append(z)
        print("u1=",u1)
        d=np.abs(ur[i][N]-uf)
        print("d=",d)
        print("")
        if d<tol:
            k+=1
            
    if len(u1)==1:
        o=u1[i]*2
        u1.append(o)
        print("u1=", u1)
        print("")
    
    i+=1
    
mpl.show()
    
