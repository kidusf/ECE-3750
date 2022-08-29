import numpy as np
import matplotlib.pyplot as plt
from math import isclose, pi, cos, sin, sqrt, atan, degrees
from matplotlib import collections as matcoll

# A= T/tau
amplitude=int(input("Choose an amplitude: "))
# type of spectrum
option=input("magnitude, phase, or inverse?: ")
# n
end=int(input("Choose the amount of terms: "))
T=float(input("Period?: "))
lines=[]
a_x=[]
a_y=[]
# from 1 to n compute a_n and b_n
added=False
signal=[]
a_0=1/2
for n in range(1, end+1):
    # compute a_n
    a_n=((T*(amplitude)**2)/((2*pi*n)**2))*(1-cos((2*pi*n)/amplitude))
    # compute b_n
    b_n=(amplitude*T/(2*pi*n))*(-1+((amplitude/(2*pi*n))*sin((2*pi*n)/amplitude)))
    if(option=="magnitude"):
        # take the magnitude using pythagorem's theorem
        pair=[(n,0), (n, sqrt(a_n**2+b_n**2))]
    elif(option=="phase"):
        # take the phase using arctan and convert from radians to degrees
        if(a_n!=0):
            pair=[(n, 0), (n, degrees(atan(b_n/a_n)))]
        else:
            theta=90 if b_n>0 else -90
            pair=[(n, 0), (n, theta)]
    else:
        c_n=sqrt(a_n**2+b_n**2)
        c_phi=pi/2 if b_n>0 else -pi/2
        if(a_n!=0):
            c_phi=atan(b_n/a_n)
        sub_signal=[]
        t=0
        while t<=4*T:
            y=c_n*cos(2*pi*t*n/T+c_phi)+a_0
            sub_signal.append(y)
            if(not added):
                a_x.append(t)
            t+=0.0001
        added=True
    if(option=="inverse"):
        signal.append(sub_signal)

    if(option=="magnitude" or option=="phase"):
        lines.append(pair)
        a_x.append(n)
    if(option=="magnitude"):
        a_y.append(sqrt(a_n**2+b_n**2))
    elif(option=="phase"):
        if(a_n!=0):
            a_y.append(degrees(atan(b_n/a_n)))
        else:
            a_y.append(90)
if(option=="magnitude" or option=="phase"):
    linecoll = matcoll.LineCollection(lines)
    fig, ax = plt.subplots()
    ax.add_collection(linecoll)
    plt.scatter(np.array(a_x), np.array(a_y))
    plt.xlabel("n")
    option=option[0].upper()+option[1:]
    degree=""
    if(option=="Phase"):
        degree+=" (degrees)"
    plt.ylabel(option+degree)
    plt.title(option+" Spectrum, A="+str(amplitude)+", n="+str(end))
else:
    y=np.sum(signal, axis=0)
    x=np.array(a_x)
    plt.plot(x,y)
    plt.title("Synthesized Signal")
    plt.xlabel("t")
    plt.ylabel("x(t)")
plt.show()
