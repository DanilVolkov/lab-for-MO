import numpy as np


def symmetrical_point(x1, x2, a):
    return x1 + a * (x2 - x1)


def average_except_one_point(arr, ind):
    return (sum(arr) - arr[ind]) / (len(arr) - 1)


def index_second_max(arr):
    sec_max = min(arr)
    m = arr.index(max(arr))
    l_arr = len(arr)
    for i in range(l_arr):
        if i != m and sec_max < arr[i]:
            sec_max = arr[i]
    return arr.index(sec_max)


def index_min_max(arr):
    return arr.index(min(arr)), arr.index(max(arr))


def shrink_points(arr_points, arr_values):
    ind_min = arr_values.index(min(arr_values))
    return symmetrical_point(arr_points, arr_points[ind_min], 0.5)


def calculate_neldermead(fun, dim, alpha=1.5, beta=1.5, gamma=1.5):
    if alpha <= 0 or beta <= 1 or gamma <= 1 or dim <= 0:
        raise RuntimeError
    simplex = np.eye(dim + 1, dim)
    while not np.isclose(simplex, simplex[0]).all():

        fun_val = [fun(x0) for x0 in simplex]

        ind_min, ind_max = index_min_max(fun_val)

        avg_x = average_except_one_point(simplex, ind_max)
        sym_x = symmetrical_point(avg_x, simplex[ind_max], -alpha)

        if fun_val[ind_min] > fun(sym_x):
            x1 = symmetrical_point(avg_x, sym_x, gamma)
            if fun(sym_x) > fun(x1):
                simplex[ind_max] = x1
            else:
                simplex[ind_max] = sym_x

        else:
            if fun_val[index_second_max(fun_val)] >= fun(sym_x):
                simplex[ind_max] = sym_x

            if fun(sym_x) < fun_val[ind_max]:
                fun_x2 = fun(sym_x)
                x2 = sym_x
            else:
                fun_x2 = fun_val[ind_max]
                x2 = simplex[ind_max]

            x3 = symmetrical_point(avg_x, x2, beta)
            if fun(x3) > fun_x2:
                simplex = shrink_points(simplex, fun_val)
            else:
                simplex[ind_max] = x3

    return np.round(sum(simplex) / (dim + 1), 5)
