import unittest


from method import func_parser as fp


class Test(unittest.TestCase):
    def test_add_math_usal(self):
        str = "sqrt exp sin cos tan log"
        add_math_str = fp.add_math(str)

        expected = "math.sqrt math.exp math.sin math.cos math.tan math.log"
        self.assertEqual(add_math_str, expected)

    def test_add_math_not_change(self):
        str = "(x1^2 + x2^2)^2"
        add_math_str = fp.add_math(str)

        expected = "(x1^2 + x2^2)^2"
        self.assertEqual(add_math_str, expected)

    def test_check_for_correct_func_negative(self):
        str = "(x1^2 + x2^2)^2 + hello world!"

        expected = Exception
        self.assertRaises(expected, fp.check_for_correct_func,
                          str)

    def test_add_brackets_and_indexes(self):
        str = "(x1^2 + x2^2)^2"
        parsed_str = fp.add_brackets_and_indexes(str)

        expected = "(x[0]^2 + x[1]^2)^2"
        self.assertEqual(parsed_str, expected)

    def test_repl_pow_sym(self):
        str = "(x1^2 + x2^2)^2"
        parsed_str = fp.repl_pow_sym(str)

        expected = "(x1**2 + x2**2)**2"
        self.assertEqual(parsed_str, expected)

    def test_count_variables(self):
        str = "(x[1]^2 + x[2]^2)^2"
        num_of_variables = fp.count_variables(str)

        expected = 2
        self.assertEqual(num_of_variables, expected)

    def test_parser(self):
        str = "(x1-1)^2+(x1-2)+sin(x1)+exp^(x3-x2)"
        parsed_str = fp.function_parsing(str)[1]
        expected = "(x[0]-1)**2+(x[0]-2)+math.sin(x[0])+math.exp**(x[2]-x[1])"
        self.assertEqual(parsed_str, expected)
