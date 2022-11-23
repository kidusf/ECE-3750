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
        f_b=1/(2*np.pi*R*C)
        if(f_b>=0.05 and f_b<=0.1 and R>=250*1000 and R<=300*1000):
            print(R, C, f_b)
print("______________________________")
print()
# integrator
for R in resistors:
    for C in capacitors:
        if(R*C>=1 and R*C<=10):
            print(R, C, R*C)
print("______________________________")
print()
# non-inverting amplifier
for R6 in resistors:
    for R7 in resistors:
        for C in capacitors:
            Rth=R6*R7/(R6+R7)
            f_b=(R6+R7)/(2*np.pi*R6*R7*C)
            v_out=3.3*R7/(R6+R7)

            if((Rth>=25000 and Rth<=100000) and(f_b>=2 and f_b<=5) and (v_out>=3.3/2*0.95 and v_out<=3.3/2*1.05)):
                print(R6, R7, C, Rth, f_b, v_out)
print("______________________________")
print()

# isolator

for R14 in resistors:
    for R12 in resistors:
        if(R12/R14>=0.69 and R12/R14<=0.773 and 2.5/(0.006*R12)<=10/1000):
            print(R12, R14, R12/R14)
print("______________________________")
print()