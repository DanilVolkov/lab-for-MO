from Nelder_Mead import NelderMead
import scipy as sp
import numpy as np

nm = NelderMead()
n = 2
x = [0] * n
f = lambda x: 2 * x[0]**4 + x[1]**4 - x[0]**2 - 2*x[1]**2
# дописать парсер
x_ans = nm.solve(f, n)
print(x_ans)
print(f(x_ans))
print(sp.optimize.minimize(f, np.ones(n)))
