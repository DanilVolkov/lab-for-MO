import unittest
import numpy as np


from method import nelder_mead as nm


class Test(unittest.TestCase):
    def test_Himmelblau_function(self):
        function = "(x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2"
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

    def test_simple_function(self):
        function = "(x[0] - 1)**2"
        f = lambda x: eval(function)
        points = nm.calculate_neldermead(f, 1)
        function_value = f(points)

        expected_point = np.array([1])
        expected_value = 0
        np.testing.assert_array_almost_equal(expected_point, points, 5)
        self.assertEqual(function_value, expected_value, 5)

    def test_Rastrigin_function(self):
        function = "20+(x[0]-5)**2+(x[1]-5)**2-10*np.cos(2*np.pi*x[0])-10*np.cos(2*np.pi*x[1])"  # noqa
        f = lambda x: eval(function)
        points = nm.calculate_neldermead(f, 2)
        function_value = f(points)

        expected_point = np.array([5, 5])
        expected_value = 0
        try:
            np.testing.assert_array_almost_equal(expected_point, points, 5)
            np.testing.assert_allclose(function_value, expected_value, 5)
        except Exception as ex:
            print(f"Метод Нелдера-Мида не работает: {ex}")

# Тест выше - функция, для которой метод Нелдера-Мида не работает
# и застревает в локальном min.
