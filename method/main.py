from nelder_mead import NelderMead
from func_parser import FuncParser
# import scipy as sp

nm = NelderMead()
ps = FuncParser()
n, func = ps.func_pars(input())
print(func)
# f = lambda x: 2 * x[0]**4 + x[1]**4 - x[0]**2 - 2*x[1]**2
f = lambda x: eval(func) # pylint is crazy about this string
x_ans = nm.calculate(f, n)
print(x_ans)
print(f(x_ans))
# s_point = np.array([0, 0])
# print(sp.optimize.minimize(f, s_point, method='Nelder-Mead'))
