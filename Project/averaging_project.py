import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize
import matplotlib as mpl

f_s=1600
e=math.e
H1=[0]*512
H1.extend([1/26]*26)
H1.extend([0]*512)
ones=[1]*1032
H2=[0]*512
H2.extend([1/27]*27)
H2.extend([0]*513)
H=np.convolve(H1, H2, "full")
zeroes=np.roots(H)
#print(zeroes)
H=np.fft.fft(H)
omega=np.linspace(start=-np.pi, stop=np.pi, num=len(H))
H=20*np.log10(np.abs(H))
f=(f_s*omega)/(2*np.pi)
plt.plot(f[len(H)//2:], H[0:len(H)//2+1])
plt.xlabel("frequency (Hz)")
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


