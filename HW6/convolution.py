import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

a_0=10
B=20
f_c=60
f=np.linspace(start=(-500), stop=(500), num=100000)
indices=[i for i in range(len(f)) if abs(f[i]-f_c)<=0.005 or abs(f[i]+f_c)<=0.005]
x=np.piecewise(f, [((f>=0)& (f<=B)), ((f<0) & (f>=-B))], [lambda f: a_0-a_0/B*f, lambda f: a_0+a_0/B*f])
c=(signal.unit_impulse(len(f), indices[0])+signal.unit_impulse(len(f), indices[1]))/2
plt.plot(f, x)
plt.plot(f, c)
y=np.convolve(x, c, 'same')
plt.plot(f, y)
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")
plt.legend(["x(t)", "h(t)", "x(t)*h(t)"])
plt.show()
y2=np.convolve(y, c, 'same')
plt.plot(f, y)
plt.plot(f, c)
plt.plot(f, y2)
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")
plt.legend(["x(t)", "h(t)", "x(t)*h(t)"])
plt.show()