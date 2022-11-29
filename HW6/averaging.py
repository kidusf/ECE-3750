import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize
import matplotlib as mpl

f_s=480
e=math.e
H1=[1/8]*8
H1.extend([0]*2048)
H2=[1/6]*6
H2.extend([0]*2050)
H=np.convolve(H1, H2, "full")
zeroes=np.roots(H)
#print(zeroes)
H=np.fft.fft(H)
omega=np.linspace(start=-np.pi, stop=np.pi, num=len(H))
H=20*np.log10(np.abs(H))
tempH=H[0:len(H)//2+1]
tempO=omega[len(H)//2:]
between=[(tempH[i], tempO[i])  for i in range(len(tempH)) if tempO[i]>=0.785398163397448 and tempO[i]<=1.047197551196598]
print(between)
max_y, max_x=max(between)
fig, ax = plt.subplots(figsize=(3, 3))
ax.plot(omega[len(H)//2:], H[0:len(H)//2+1])
ax.annotate('max point between 60 and 80 Hz: ('+str(round(max_x, 4))+" radians, "+str(round(max_y,4))+" dB, " +str(round(f_s*max_x/(2*np.pi), 4))+" Hz)",
            xy=(max_x, max_y), xycoords='data',
            xytext=(max_x, max_y), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
plt.xlabel("frequency (radians)")
plt.ylabel("| H | (dB)")

#plt.legend(["60 Hz", "80 Hz", "combined"])
plt.title("Frequency response of the FIR filters")
plt.show()

# extract real part
x = [zero.real for zero in zeroes ]
# extract imaginary part
y = [zero.imag for zero in zeroes]

mpl.rcParams['axes.linewidth'] = 0.1
# plot the complex numbers
plt.scatter(x, y, facecolors='none', edgecolors='r')
plt.scatter(0, 0, marker="x")
plt.xlim(right=1)
plt.legend(["zeroes", "poles"])
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()


