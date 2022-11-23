from cmath import inf
from math import log10
import numpy as np
import matplotlib.pyplot as plt

# use a fixed value for bandwidth in order to plot
B=100
# go from 0 Hz to 1.2 B Hz
f=np.linspace(start=0, stop=1.2*B)

# contains the smallest N to meet specifications
min_order=float(inf)
# this will hold the alpha and N that meet specifications with N being as small as possible
res=[0, 0]

# go from 1 to 50
for N in range(1, 51):
    # go from f=B to f=1.2 B because the corner frequency must be in between those bounds
    alpha=1
    while alpha<=1.2:
        # compute the amount of dB down the bandwidth is
        M_band=20*np.log10(1/np.sqrt(1+(1/alpha)**(2*N)))
        # compute the amount of dB down after 1.2 B Hz 
        M_fall=20*np.log10(1/np.sqrt(1+(1.2/alpha)**(2*N)))
        # check if the bandwidth does not fall to -0.25 dB or less and after 1.2 B Hz, it is -60 dB down or less.
        # We can assume that the gain is no more than 0 dB .
        if(M_band>-0.25 and M_fall<-60 and N<min_order):
            # keep track of the lowest order filter
            min_order=N
            res=[alpha, N]
    

        alpha+=0.001
n=res[1]
a=res[0]
# verify that the N and alpha meet specifications
assert 20*np.log10(1/np.sqrt(1+(B/(a*B))**(2*n)))>-0.25 and 20*np.log10(1/np.sqrt(1+(1.2*B/(a*B))**(2*n)))
print(n, a, a*B)
# find the transfer function
M=20*np.log10(1/np.sqrt(1+(f/(a*B))**(2*n)))
# annotate the plot with points at B, f_c, and 1.2 B
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
