import numpy as np
import matplotlib.pyplot as mpl

a=5
b=8
n=4
h=(b-a)/n
tol=10**(-5)

yp=[-0.00026538]
ys=0.0038731
y=[]
ye=0.0030770
x=np.arange(a,b+h,h)
print('x=', x)
print("")

#######################################################################
#RK4

def f1(x,y1,y2):
    return y2

def f2(x,y1,y2):
    return -y2/x+y1/x**2
    
def k11(x,y1,y2):
    return f1(x,y1,y2)

def k12(x,y1,y2):
    return f2(x,y1,y2)

def k21(x,y1,y2,h):
    return f1(x+h/2,y1+h*k11(x,y1,y2)/2,y2+h*k12(x,y1,y2)/2)

def k22(x,y1,y2,h):
    return f2(x+h/2,y1+h*k11(x,y1,y2)/2,y2+h*k12(x,y1,y2)/2)

def k31(x,y1,y2,h):
    return f1(x+h/2,y1+h*k21(x,y1,y2,h),y2+h*k22(x,y1,y2,h)/2)

def k32(x,y1,y2,h):
    return f2(x+h/2,y1+h*k21(x,y1,y2,h),y2+h*k22(x,y1,y2,h)/2)

def k41(x,y1,y2,h):
    return f1(x+h,y1+h*k31(x,y1,y2,h),y2+h*k32(x,y1,y2,h))

def k42(x,y1,y2,h):
    return f2(x+h,y1+h*k31(x,y1,y2,h),y2+h*k32(x,y1,y2,h))

def rk41(x,y1,y2,h):
    return y1+(1/6)*(k11(x,y1,y2)+2*k21(x,y1,y2,h)+2*k31(x,y1,y2,h)+k41(x,y1,y2,h))

def rk42(x,y1,y2,h):
    return y2+(1/6)*(k12(x,y1,y2)+2*k22(x,y1,y2,h)+2*k32(x,y1,y2,h)+k42(x,y1,y2,h))

j=0
k=0

while j==0:
    print("y'=",yp[j])
    v1=[]
    v2=[]
    v1.append(ys)
    v2.append(yp[k])
    for i in range (0,len(x)-1):
        g=rk41(x[i],v1[i],v2[i],h)
        m=rk42(x[i],v1[i],v2[i],h)
        #g=v1[i]+f1(x[i], v1[i], v2[i])*h #euler's
        #m=v2[i]+f2(x[i], v1[i], v2[i])*h #method
        v1.append(g)
        v2.append(m)
    y.append(v1)


    print('y1=', v1)
    print('y2=', v2)
    print("")
    mpl.plot(x,v1)


    if len(yp)>1:
        z=yp[k-1]+(yp[k]-yp[k-1])*(ye-y[k-1][n])/(y[k][n]-y[k-1][n])
        yp.append(z)
        print("y'=",yp)
        print("y(",b,")=", y[k][n])
        d=np.abs(y[k][n]-ye)
        print("d=",d)
        print("")
        if d<tol:
            j+=1
    
   
    if len(yp)==1:
        o=yp[k]*2
        yp.append(o)
    
    k+=1

mpl.show()


     