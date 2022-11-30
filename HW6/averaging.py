import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize, signal
import matplotlib as mpl
import scipy

f_s=480
e=math.e
H1=[1/8]*8
H1.extend([0]*2048)
H2=[1/6]*6
H2.extend([0]*2050)
H=np.convolve(H2, H1, "full")
zeroes=np.roots(H)
#print(zeroes)
H=list(np.fft.fft(H))
H=H[len(H)//2:]+H[0:len(H)//2+1]
H=np.array(H)

omega=np.linspace(start=-np.pi, stop=np.pi, num=len(H))
print(omega[0])
H=20*np.log10(np.abs(H))
between=[(H[i], omega[i])  for i in range(len(H)) if omega[i]>=0.785398163397448 and omega[i]<=1.047197551196598]
#print(between)
max_y, max_x=max(between)
fig, ax = plt.subplots(figsize=(3, 3))
ax.plot(omega, H)
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


