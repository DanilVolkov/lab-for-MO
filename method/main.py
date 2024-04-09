from Nelder_Mead import NelderMead
from FuncParser import FuncParser
#import scipy as sp
import numpy as np

nm = NelderMead()
ps = FuncParser()
n = 2
x = [0] * n

n , func = ps.func_pars(input())
print(func)
#f = lambda x: 2 * x[0]**4 + x[1]**4 - x[0]**2 - 2*x[1]**2
f = lambda x: eval(func)

x_ans = nm.calculate(f, n)
print(x_ans)
print(f(x_ans))
""" s_point = np.array([0, 0])
print(sp.optimize.minimize(f, s_point, method='Nelder-Mead')) """
