from cmath import inf
from math import log10
import numpy as np
import matplotlib.pyplot as plt

B=100
f=np.linspace(start=0, stop=1.2*B)


min_order=float(inf)
res=[0, 0]
for N in range(1, 71):
    alpha=1
    while alpha<=1.2:
        M_band=20*np.log10(1/np.sqrt(1+(1/alpha)**(2*N)))
        M_fall=20*np.log10(1/np.sqrt(1+(1.2/alpha)**(2*N)))
        if(M_band>-0.25 and M_fall<-60 and N<min_order):
            min_order=N
            res=[alpha, N]
    

        alpha+=0.001
n=res[1]
a=res[0]
assert 20*np.log10(1/np.sqrt(1+(B/(a*B))**(2*n)))>-0.25 and 20*np.log10(1/np.sqrt(1+(1.2*B/(a*B))**(2*n)))
print(n, a, a*B)
M=20*np.log10(1/np.sqrt(1+(f/(a*B))**(2*n)))
fig, ax = plt.subplots(figsize=(8, 5))
ax.annotate(
    ' ('+str(np.round(a*B, 3))+" Hz ,"+str(np.round(20*np.log10(1/np.sqrt(1+1)), 3))+ " dB)",
    xy=(a*B, -3.01), xycoords='data',
    xytext=(a*B/10, 10), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.annotate(
    '('+str(np.round(B, 3))+" Hz, "+str(np.round(20*np.log10(1/np.sqrt(1+(B/(a*B))**(2*n))), 3))+" dB)", 
    xy=(B, 20*np.log10(1/np.sqrt(1+(B/(a*B))**(2*n)))), xycoords='data',
    xytext=(B/10, 10), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.annotate(
    '('+str(np.round(1.2*B, 3))+" Hz, "+str(np.round(20*np.log10(1/np.sqrt(1+(1.2*B/(a*B))**(2*n))), 3))+" dB)", 
    xy=(1.2*B, 20*np.log10(1/np.sqrt(1+(1.2*B/(a*B))**(2*n)))), xycoords='data',
    xytext=(1.2*B/10, 10), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.semilogx(f, M)
plt.title("Bode plot for Q3, B= "+str(B))
plt.xlabel("Frequency, f(Hz)")
plt.ylabel("Magnitude(dB)")
plt.show()
