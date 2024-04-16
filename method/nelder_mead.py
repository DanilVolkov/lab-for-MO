import numpy as np


def symmetrical_point(x1, x2, a):
    return x1 + a * (x2 - x1)


def average_except_one_point(array, exception_index):
    return (sum(array) - array[exception_index]) / (len(array) - 1)


def index_second_max(array):
    second_max = min(array)
    index_max = array.index(max(array))
    len_array = len(array)
    for i in range(len_array):
        if i != index_max and second_max < array[i]:
            second_max = array[i]
    return array.index(second_max)


def index_min_max(array):
    return array.index(min(array)), array.index(max(array))


def shrink_points(array_points, array_values):
    index_min = array_values.index(min(array_values))
    return symmetrical_point(array_points, array_points[index_min], 0.5)


def calculate_neldermead(function, dimension, alpha=1.5, beta=1.5, gamma=1.5):
    if alpha <= 0 or beta <= 1 or gamma <= 1 or dimension <= 0:
        raise RuntimeError
    simplex = np.eye(dimension + 1, dimension)
    while not np.isclose(simplex, simplex[0]).all():

        function_value = [function(x0) for x0 in simplex]

        index_min, index_max = index_min_max(function_value)

        average_x = average_except_one_point(simplex, index_max)
        symmetrical_x = symmetrical_point(average_x, simplex[index_max], -alpha)

        if function_value[index_min] > function(symmetrical_x):
            x1 = symmetrical_point(average_x, symmetrical_x, gamma)
            if function(symmetrical_x) > function(x1):
                simplex[index_max] = x1
            else:
                simplex[index_max] = symmetrical_x

        else:
            if function_value[index_second_max(function_value)] >= function(symmetrical_x):
                simplex[index_max] = symmetrical_x

            if function(symmetrical_x) < function_value[index_max]:
                function_x2 = function(symmetrical_x)
                x2 = symmetrical_x
            else:
                function_x2 = function_value[index_max]
                x2 = simplex[index_max]

            x3 = symmetrical_point(average_x, x2, beta)
            if function(x3) > function_x2:
                simplex = shrink_points(simplex, function_value)
            else:
                simplex[index_max] = x3

    return np.round(sum(simplex) / (dimension + 1), 5)
