import re


def add_math(func: str) -> str:
    patterns = ["sqrt", "exp", "sin", "cos", "tan", "pi"]
    for pattern in patterns:
        func = re.sub(pattern, "math." + pattern, func)
    func = replace_log(func)
    return func


def check_for_correct_func(func: str) -> None:
    allowed_char_pattern = r"[^acegilnopqrstx\^0-9\(\)\+\-\/\*,\. ]"
    if len(re.findall(allowed_char_pattern, func)) != 0:
        raise Exception("Строка некорректна")


def add_brackets_and_indexes(func: str) -> str:
    pattern_for_x = r"x\d+"
    x_group = re.findall(pattern_for_x, func)
    for i in range(len(x_group)):
        numb = "x[" + str(int(x_group[i][1]) - 1) + "]"
        func = re.sub(pattern_for_x, numb, func, 1)
    return func


def repl_pow_sym(func: str) -> str:
    return re.sub(r"\^", "**", func)


def count_variables(func: str) -> int:
    pattern_for_var = r"(?<=\[)\d+(?=\])"
    return len(set(re.findall(pattern_for_var, func)))


def replace_log(func: str) -> str:
    func = re.sub("ln", "np.log", func)
    func = re.sub("log", "np.emath.logn", func)
    return func


def function_parsing(func: str) -> tuple[int, str]:
    check_for_correct_func(func)
    func = add_brackets_and_indexes(func)
    func_result = repl_pow_sym(func)
    func_result = add_math(func_result)
    dimensions = count_variables(func_result)
    return dimensions, func_result
