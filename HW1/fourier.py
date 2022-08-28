import numpy as np
import matplotlib.pyplot as plt
from math import isclose, pi, cos, sin, sqrt, atan, degrees
from matplotlib import collections as matcoll


# A= T/tau
amplitude=int(input("Choose an amplitude: "))
# type of spectrum
option=input("magnitude or phase?: ")
# n
end=int(input("Choose the amount of terms: "))
lines=[]
a_x=[]
a_y=[]
# from 1 to n compute a_n and b_n
for n in range(1, end+1):
    # compute a_n
    a_n=((2*(amplitude)**2)/((2*pi)**2))*(1-cos((2*pi*n)/amplitude))
    # compute b_n
    b_n=(amplitude/pi)*(1-(1/(2*pi)*sin((2*pi*n)/amplitude)))
    if(option=="magnitude"):
        # take the magnitude using pythagorem's theorem
        pair=[(n,0), (n, sqrt(a_n**2+b_n**2))]
    else:
        # take the phase using arctan and convert from radians to degrees
        pair=[(n, 0), (n, degrees(atan(b_n/a_n)))]

    lines.append(pair)
    a_x.append(n)
    if(option=="magnitude"):
        a_y.append(sqrt(a_n**2+b_n**2))
    else:
        a_y.append(degrees(atan(b_n/a_n)))

linecoll = matcoll.LineCollection(lines)
fig, ax = plt.subplots()
ax.add_collection(linecoll)

plt.scatter(np.array(a_x), np.array(a_y))
plt.xlabel("n")
option=option[0].upper()+option[1:]
plt.ylabel(option)
plt.title(option+" Spectrum, A="+str(amplitude))
plt.show()
