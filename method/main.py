from nelder_mead import calculate_neldermead
from func_parser import FuncParser
# import scipy as sp

with open('input.txt', 'r', encoding='UTF-8') as file:
    s = file.readline()
n, func = FuncParser.func_pars(s)
print(func)
f = lambda x: eval(func)
x_ans = calculate_neldermead(f, n)
print(x_ans)
print(f(x_ans))
# s_point = np.array([0, 0])
# print(sp.optimize.minimize(f, s_point, method='Nelder-Mead'))
