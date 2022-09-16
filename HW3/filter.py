from cmath import inf
from math import log10
import numpy as np
import matplotlib.pyplot as plt

B=100
f=np.linspace(start=0, stop=1.2*B)


min_order=float(inf)
res=[0, 0]
for N in range(1, 71):
    alpha=0.01
    while alpha<=100:
        M_band=20*np.log10(1/np.sqrt(1+(1/alpha)**(2*N)))
        M_fall=20*np.log10(1/np.sqrt(1+(1.2/alpha)**(2*N)))
        if(M_band>-0.25 and M_fall<-60 and N<min_order):
            min_order=N
            res=[alpha, N]
    

        alpha+=0.01
n=res[1]
a=res[0]
assert 20*np.log10(1/np.sqrt(1+(B/(a*B))**(2*n)))>-0.25 and 20*np.log10(1/np.sqrt(1+(1.2*B/(a*B))**(2*n)))
print(n, a)
M=20*np.log10(1/np.sqrt(1+(f/(a*B))**(2*n)))
plt.semilogx(f, M)
plt.title("Bode plot for Q3, B= "+str(B))
plt.xlabel("Frequency, f(Hz)")
plt.ylabel("Magnitude(dB)")
plt.show()
