import numpy as np
import pandas as pd

data=pd.read_excel("ComponentList.xlsx")
resistors=data["R"]
capacitors=data["C"]
capacitors.dropna(inplace=True)
capacitors=list(capacitors)
resistors=list(resistors)

# RC input
for R in resistors:
    for C in capacitors:
        if(1/(2*np.pi*R*C)>=0.05 and 1/(2*np.pi*R*C)<=0.1):
            print(R, C)
print("______________________________")
print()
# integrator
for R in resistors:
    for C in capacitors:
        if(R*C>=1 and R*C<=10):
            print(R, C)
print("______________________________")
print()
# non-inverting amplifier
for R6 in resistors:
    for R7 in resistors:
        for C in capacitors:
            Rth=R6*R7/(R6+R7)
            f_b=(R6+R7)/(2*np.pi*R6*R7*C)
            gain=1/(R6*C)

            if((Rth>=25000 and Rth<=100000) and(f_b>=2 and f_b<=5) and (gain>=3.3/2*0.95 and gain<=3.3/2*1.05)):
                print(R6, R7, C)
print("______________________________")
print()
