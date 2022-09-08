import numpy as np
import matplotlib.pyplot as plt
from math import isclose, pi, cos, sin, sqrt, atan, degrees
from matplotlib import collections as matcoll
import scipy.integrate as integrate

# A= T/tau
amplitude=int(input("Choose an amplitude: "))
# type of spectrum
option=input("magnitude, phase, or inverse?: ")
# n
end=int(input("Choose the amount of terms: "))
T=float(input("Period?: "))
tau=T/amplitude
lines=[]
a_x=[]
a_y=[]
# from 1 to n compute a_n and b_n
added=False
signal=[]
a_0=1/T *integrate.quad(lambda t: amplitude-(amplitude/tau)*t, 0, tau)[0] 
for n in range(1, end+1):
    # compute a_n
    a_n= integrate.quad(lambda t: (amplitude-(amplitude/tau)*t)*cos(n*2*pi*t/T) , 0, tau)[0]
    a_n=a_n*2/T
    # compute b_n
    b_n=integrate.quad(lambda t: (amplitude-(amplitude/tau)*t)*sin(n*2*pi*t/T) , 0, tau)[0]
    b_n=b_n*2/T
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
    # reconstruct the signal by computing c_n and #c_phi
    else:
        c_n=sqrt(a_n**2+b_n**2)
        c_phi=pi/2 if b_n>0 else -pi/2
        if(a_n!=0):
            c_phi=-atan(b_n/a_n)
        sub_signal=[]
        t=0
        # make a subsignal of 1 period 
        while t<=T:
            y=c_n*cos(2*pi*t*n/T+c_phi)
            sub_signal.append(y)
            if(not added):
                a_x.append(t)
            t+=0.0001
        added=True
    # add the subsignal to the signal
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
            theta= 90 if b_n>0 else -90
            a_y.append(theta)
# create a scatter plot for magnitude and phase
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
    # sum up all of the subsignals and construct a line plot
    y=np.sum(signal, axis=0)
    y+=a_0
    x=np.array(a_x)
    plt.plot(x,y)
    plt.title("Synthesized Signal, T="+str(T)+" seconds")
    plt.xlabel("t")
    plt.ylabel("x(t)")
plt.show()
