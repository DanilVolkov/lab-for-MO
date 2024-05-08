import re


def add_np(func_str):
    patterns = ["sqrt", "exp", "sin", "cos", "tan", "pi"]
    for pattern in patterns:
        func_str = re.sub(pattern, "np." + pattern, func_str)
    func_str = replace_log(func_str)
    return func_str


def check_for_correct_func(func_str):
    allowed_char_pattern = r"[^acegilnopqrstx\^0-9\(\)\+\-\/\*,\. ]"
    if len(re.findall(allowed_char_pattern, func_str)) != 0:
        raise Exception("Строка некорректна")


def add_brackets_and_indexes(func_str):
    pattern_for_x = r"x\d+"
    x_group = re.findall(pattern_for_x, func_str)
    for i in range(len(x_group)):
        numb = "x[" + str(int(x_group[i][1]) - 1) + "]"
        func_str = re.sub(pattern_for_x, numb, func_str, 1)
    return func_str


def repl_pow_sym(func_str):
    return re.sub(r"\^", "**", func_str)


def count_variables(func_str):
    pattern_for_var = r"(?<=\[)\d+(?=\])"
    return len(set(re.findall(pattern_for_var, func_str)))


def replace_log(func_str):
    func_str = re.sub("ln", "np.log", func_str)
    func_str = re.sub("log", "np.emath.logn", func_str)
    return func_str


def function_parsing(func_str):
    check_for_correct_func(func_str)
    func_str = add_brackets_and_indexes(func_str)
    func_str = repl_pow_sym(func_str)
    func_str = add_np(func_str)
    dimensions = count_variables(func_str)
    return dimensions, func_str
