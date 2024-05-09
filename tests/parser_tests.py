import unittest


from method import func_parser as fp


class Test(unittest.TestCase):
    def test_add_np_usal(self):
        str = "sqrt exp sin cos tan log"
        add_math_str = fp.add_np(str)

        expected = "np.sqrt np.exp np.sin np.cos np.tan np.emath.logn"
        self.assertEqual(add_math_str, expected)

    def test_add_np_not_change(self):
        str = "(x1^2 + x2^2)^2"
        add_math_str = fp.add_np(str)

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
        with open("tests/test_func.txt") as file:
            str = file.read().rstrip('\n')
        # str = "(x1-1)^2+(x1-2)+sin(x1)+exp^(x3-x2)"
        with open("tests/out_test_func.txt") as file:
            expected = file.read().rstrip('\n')
        parsed_str = fp.function_parsing(str)[1]
        # expected = "(x[0]-1)**2+(x[0]-2)+np.sin(x[0])+np.exp**(x[2]-x[1])"
        self.assertEqual(parsed_str, expected)

    def test_replace_log(self):
        str = "ln(x1) + ln(x2) + 4*log(5, x1)"
        replace_log = fp.replace_log(str)

        expected = "np.log(x1) + np.log(x2) + 4*np.emath.logn(5, x1)"
        self.assertEqual(replace_log, expected)
