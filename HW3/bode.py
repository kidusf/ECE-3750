import numpy as np
import matplotlib.pyplot as plt

poles = [-10, -1000]
zeros = [0]
omega=np.logspace(start=-2, stop=5, base=10)
s=1j*omega
numerator=1 if len(zeros)==0 else np.absolute(s-zeros[0])
denominator= 1 if len(poles)==0 else  np.absolute(s-poles[0] )
for i in range(1, len(zeros)):
    numerator=numerator * np.absolute((s-zeros[i]))
for k in range(1, len(poles)):
    denominator= denominator * np.absolute((s-poles[k]))
#print(numerator, denominator)

H=numerator/denominator
print(H)
H=20*np.log10(H)
plt.semilogx(omega, H)
plt.show()
