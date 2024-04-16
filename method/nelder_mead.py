import numpy as np


def sym_point(x1, x2, a):
    return x1 + a * (x2 - x1)


def avg_but_one_point(arr, ind):
    return (sum(arr) - arr[ind]) / (len(arr) - 1)


def ind_sec_max(arr):
    sec_max = min(arr)
    m = arr.index(max(arr))
    l_arr = len(arr)
    for i in range(l_arr):
        if i != m and sec_max < arr[i]:
            sec_max = arr[i]
    return arr.index(sec_max)


def ind_min_max(arr):
    return arr.index(min(arr)), arr.index(max(arr))


def shrink_points(arr_p, arr_f):
    ind_min = arr_f.index(min(arr_f))
    return sym_point(arr_p, arr_p[ind_min], 0.5)


def calculate_neldermead(fun, n, alpha=1.5, beta=1.5, gamma=1.5):
    if alpha <= 0 or beta <= 1 or gamma <= 1 or n <= 0:
        raise RuntimeError
    simp = np.eye(n + 1, n)
    while not np.isclose(simp, simp[0]).all():
        fun_val = [fun(x0) for x0 in simp]
        ind_min, ind_max = ind_min_max(fun_val)
        avg_x = avg_but_one_point(simp, ind_max)
        sym_x = sym_point(avg_x, simp[ind_max], -alpha)
        if fun_val[ind_min] > fun(sym_x):
            x1 = sym_point(avg_x, sym_x, gamma)
            if fun(sym_x) > fun(x1):
                simp[ind_max] = x1
            else:
                simp[ind_max] = sym_x
        else:
            if fun_val[ind_sec_max(fun_val)] >= fun(sym_x):
                simp[ind_max] = sym_x
            if fun(sym_x) < fun_val[ind_max]:
                fun_x2 = fun(sym_x)
                x2 = sym_x
            else:
                fun_x2 = fun_val[ind_max]
                x2 = simp[ind_max]
            x3 = sym_point(avg_x, x2, beta)
            if fun(x3) > fun_x2:
                simp = shrink_points(simp, fun_val)
            else:
                simp[ind_max] = x3
    return np.round(sum(simp) / (n + 1), 5)
