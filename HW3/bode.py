import numpy as np
import matplotlib.pyplot as plt

poles=[0]
zeros=[]
# range for omega
omega=np.logspace(start=-2, stop=7, base=10)

# subsitute j*w with s
s=1j*omega

# check if there are no poles or no zeroes. If  there is a pole or if there is a zero, 
# start the numerator at the first zero and start the denominator as the first es
numerator=1 if len(zeros)==0 else np.absolute(s-zeros[0])
denominator= 1 if len(poles)==0 else  np.absolute(s-poles[0] )

# go through the rest of the zeroes
for i in range(1, len(zeros)):
    # perform element wise multiplication on the magnitude of the zeroes
    numerator=numerator * np.absolute((s-zeros[i]))
# go through the rest of the poles
for k in range(1, len(poles)):
    # perform element wise multiplication on the magnitude of the poles
    denominator= denominator * np.absolute((s-poles[k]))
# perform element wise division with the numerator and denominator
H=numerator/(1*denominator)
# convert to decibels
H=20*np.log10(H)
# plot
plt.semilogx(omega, H)
plt.title("H(jw)")
plt.xlabel("w ( rad/s)")
plt.ylabel("Magnitude")
plt.show()
