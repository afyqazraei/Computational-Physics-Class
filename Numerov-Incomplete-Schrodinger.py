import numpy as np
import matplotlib.pyplot as plt

# setup the constants

hbar =   1.
k    =   0.1
h    =   0.5
xi   =  -3.
xf   =   3.
E    =  1000.
m    =   1. 

def V(x):              # potential function

    return 0.5*k*(x**2) 

def k2(x):            #  k (or q) function in Numerov method
	
	return 2*m*(E-V(x))/(hbar**2)

def S(x):            # S function in Numerov method

	return 0

def numerov(xj, xk, xl, yj, yk):   # Full polynomial of Numerov method
 
    ym = ( 2*(1 - (5/12)*(h**2)*k2(xk))*yk - (1 + (h**2)*k2(xj)/12)*yj + S(xk) )/( 1 + (h**2)*k2(xl))

    return ym

# initialize required arrays

x = np.arange(xi, xf+h, h)

z = [] 

y = [0., 1.]

# loop over the values of x

for i, ix in enumerate(x):
    
    knew = 0
    knew = V(ix)
    z.append(knew)

    if ix != xi and ix != xf:
                
        ynew = 0
        ynew = numerov(x[i-1], x[i], x[i+1], y[i-1], y[i])
        y.append(ynew)

plt.plot(x, z, 'b') # plot the potential
plt.plot(x, y, 'g') # plot the wavefunction
plt.show()
