import numpy as np
import matplotlib.pyplot as plt
import math

f_s=480
omega=np.linspace(start=-np.pi, stop=np.pi, num=1024)
s=1j*omega
e=math.e
z=np.cos(omega)+1j*np.sin(omega)

def plot(num_samples):
    numerator=np.array([0+0j]*len(omega))
    for i in range(num_samples):
        numerator=numerator+z**(-i)
    H=numerator/num_samples
    #plt.semilogx((omega/2/np.pi)*f_s, 20*np.log10(np.abs(H)))
    return H
H1=plot(8)
H2=plot(6)
H=H1*H2
f=(omega/2/np.pi)*f_s
H=20*np.log10(np.abs(H))
between=[(H[i], f[i])  for i in range(len(H)) if f[i]>=60 and f[i]<=80]
max_y, max_x=max(between)
fig, ax = plt.subplots(figsize=(3, 3))
ax.semilogx(f, H)
ax.annotate('max point between 60 and 80 Hz: ('+str(round(max_x, 4))+" Hz, "+str(round(max_y,4))+" dB)",
            xy=(max_x, max_y), xycoords='data',
            xytext=(max_x, max_y), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
plt.xlabel("frequency (Hz)")
plt.ylabel("| H | (dB)")

#plt.legend(["60 Hz", "80 Hz", "combined"])
plt.title("Frequency response of the FIR filters")
plt.show()


