from nelder_mead import calculate_neldermead
from func_parser import function_parsing
import numpy as np   # noqa F401


print(np.emath.logn(14, 0))
with open("method/input.txt") as file:
    for line in file:
        function = line.rstrip('\n')
        print(function)
        dimensions, function_parsed = function_parsing(function)
        function_x = lambda x: eval(function_parsed)
        point = calculate_neldermead(function_x, dimensions)
        print(*point)
        print(function_x(point))
