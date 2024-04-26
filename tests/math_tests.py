import unittest
import numpy as np


from method import nelder_mead as nm


class Test(unittest.TestCase):
    def test_Himmelblau_function(self):
        function = "(x[0]**2 + x[1] -11)**2 + (x[0] + x[1]**2 - 7)**2"
        f = lambda x: eval(function)
        points = nm.calculate_neldermead(f, 2)
        function_value = f(points)

        expected_point = np.array([3, 2])
        expected_value = 0
        np.testing.assert_array_almost_equal(expected_point, points, 5)
        self.assertAlmostEqual(function_value, expected_value, 5)

    def test_Rosenbrock_function(self):
        function = "(1 - x[0])**2 + 100*(x[1] - x[0]**2)**2"
        f = lambda x: eval(function)
        points = nm.calculate_neldermead(f, 2)
        function_value = f(points)

        expected_point = np.array([1, 1])
        expected_value = 0
        np.testing.assert_array_almost_equal(expected_point, points, 5)
        self.assertEqual(function_value, expected_value, 5)


"""     def test_Shaffer_function_N2(self):
        function = "0.5 + ((math.sin(x[0]**2 - x[1]**2)**2 - 0.5))/
                                (1 + 0.0001*(x[0]**2 + x[1]**2)**2)"
        f = lambda x: eval(function)
        points = nm.calculate_neldermead(f, 2)
        function_value = f(points)

        expected_point = np.array([0, 0])
        expected_value = 0
        np.testing.assert_array_almost_equal(expected_point, points, 3)
        self.assertAlmostEqual(function_value, expected_value, 3) """
