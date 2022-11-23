from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol, plot
from sympy.abc import s, t
import matplotlib.pyplot as plt
import numpy as np

# Using inverse_laplace_transform() method
h1=(403.25/(0.2*s**3+s**2+20.1625*s))
h2=((20*10.5*1.25)/((0.1*s**3)+(s**2)+(13.125*s)))

"""
gfg = inverse_laplace_transform(h1, s, t)
gfg2 = inverse_laplace_transform(h2, s, t)
"""
gfg= inverse_laplace_transform(h1, s, t)
print(gfg)
