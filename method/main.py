from nelder_mead import calculate_neldermead
from func_parser import function_parsing

function = "x1**2 + x1*x2 + x2**2 - 6*x1 - 9*x2"
dimensions, function_parsed = function_parsing(function)
function_x = lambda x: eval(function_parsed)
point = calculate_neldermead(function_x, dimensions)
print(point)
print(function_x(point))