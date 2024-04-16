import numpy as np


def sym_point(x1, x2, a):
    return x1 + a * (x2 - x1)


def find_premax(arr):
    i_max = max(arr)
    pre_max = min(arr)
    l = len(arr)
    for i in range(l):
        if i != i_max and pre_max < arr[i]:
            pre_max = arr[i]
    return pre_max


def find_avg(arr, ind):
    return (sum(arr) - arr[ind]) / (len(arr) - 1)


def calculate_neldermead(fun, n, alpha=1.5, beta=1.5, gamma=1.5):
    simp = np.eye(n + 1, n)
    while not np.isclose(simp, simp[0]).all():
        fun_val = [fun(x0) for x0 in simp]
        fun_min = min(fun_val)
        fun_max = max(fun_val)
        i_max = fun_val.index(fun_max)
        avg_x = find_avg(simp, i_max)
        sym_x = sym_point(avg_x, simp[i_max], -alpha)
        fun_sym = fun(sym_x)
        if fun_min > fun_sym:
            x1 = sym_point(avg_x, sym_x, gamma)
            if fun_sym > fun(x1):
                simp[fun_val.index(fun_max)] = x1
            else:
                simp[fun_val.index(fun_max)] = sym_x
        else:
            fun_premax = find_premax(fun_val)
            if fun_premax >= fun_sym:
                simp[i_max] = sym_x
            if fun_sym < fun_max:
                fun_x2 = fun_sym
                x2 = sym_x
            else:
                fun_x2 = fun_max
                x2 = simp[i_max]
            x3 = sym_point(avg_x, x2, beta)
            fun_x3 = fun(x3)
            if fun_x3 > fun_x2:
                simp = sym_point(simp, fun_val.index(fun_min), 0.5)
            else:
                simp[i_max] = x3
    return np.round(sum(simp) / len(simp), 5)
