import unittest
import numpy as np

from method import nelder_mead as nm
from method import func_parser as fp


class Test(unittest.TestCase):
    def test_symmetrical_point_usual(self):
        x1 = np.array([0, 1])
        x2 = np.array([1, 0])
        a = 2

        result = nm.symmetrical_point(x1, x2, a)
        expected = np.array([2, -1])

        np.testing.assert_array_equal(expected, result)

    def test_symmetrical_point_zeroes(self):
        x1 = np.zeros((2, 1))
        x2 = np.zeros((2, 1))
        a = 0

        result = nm.symmetrical_point(x1, x2, a)
        expected = np.zeros((2, 1))

        np.testing.assert_array_equal(expected, result)

    def test_symmetrical_point_negative(self):
        x1 = np.array([-1, 0])
        x2 = np.array([0, -1])
        a = 2

        result = nm.symmetrical_point(x1, x2, a)
        expected = np.array([1, -2])

        np.testing.assert_array_equal(expected, result)

    def test_symmetrical_point_same(self):
        x1 = np.array([2, 2])
        x2 = np.array([2, 2])
        a = 2

        result = nm.symmetrical_point(x1, x2, a)
        expected = np.array([2, 2])

        np.testing.assert_array_equal(expected, result)

    def test_average_point_usual(self):
        points = np.array([[1, 2], [2, 3], [3, 4]])
        except_index = 1

        result = nm.average_except_one_point(points, except_index)
        expected = np.array([2, 3])

        np.testing.assert_array_equal(expected, result)

    def test_average_point_error_raise(self):
        points = np.array([[1, 2], [2, 3], [3, 4]])
        except_index = -1

        expected = Exception

        self.assertRaises(expected, nm.average_except_one_point,
                          points, except_index)

    def test_second_max_usual(self):
        array = [1, 2, 3, 4, 5, -453]

        result = nm.index_second_max(array)
        expected = 3

        self.assertEqual(expected, result)

    def test_second_max_same_values(self):
        array = [1, 1, 1, 1, 1, 1]

        result = nm.index_second_max(array)
        expected = 0

        self.assertEqual(expected, result)

    def test_second_max_negative(self):
        array = [-1213, -23212, -223, -4, -5, -453]

        result = nm.index_second_max(array)
        expected = 4

        self.assertEqual(expected, result)

    def test_second_max_one_element_array(self):
        array = [151]

        result = nm.index_second_max(array)
        expected = 0

        self.assertEqual(expected, result)

    def test_second_max_one_empty_array(self):
        array = []

        result = nm.index_second_max(array)
        expected = -1

        self.assertEqual(expected, result)

    def test_min_max_usual(self):
        array = [1, 2, 3, 4]

        result_min, result_max = nm.index_min_max(array)
        expected_min, expected_max = 0, 3

        self.assertEqual(expected_min, result_min)
        self.assertEqual(expected_max, result_max)

    def test_min_max_same_values(self):
        array = [1, 1, 1, 1]

        result_min, result_max = nm.index_min_max(array)
        expected_min, expected_max = 0, 0

        self.assertEqual(expected_min, result_min)
        self.assertEqual(expected_max, result_max)

    def test_min_max_array_of_one_element(self):
        array = [49]

        result_min, result_max = nm.index_min_max(array)
        expected_min, expected_max = 0, 0

        self.assertEqual(expected_min, result_min)
        self.assertEqual(expected_max, result_max)

    def test_min_max_empty_array(self):
        array = []

        result_min, result_max = nm.index_min_max(array)
        expected_min, expected_max = -1, -1

        self.assertEqual(expected_min, result_min)
        self.assertEqual(expected_max, result_max)

    def test_shrink_usual(self):
        array = np.array([[2, 0], [0, 2], [-2, 0], [0, -2], [0, 0]])

        result = nm.shrink_points(array, 4)
        expected = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]])

        np.testing.assert_array_equal(expected, result)

    def test_shrink_zeros(self):
        array = np.zeros((2, 5))

        result = nm.shrink_points(array, 0)
        expected = np.zeros((2, 5))

        np.testing.assert_array_equal(expected, result)

    def test_shrink_same_values(self):
        array = np.array([243, 243, 243])

        result = nm.shrink_points(array, 0)
        expected = np.array([243, 243, 243])

        np.testing.assert_array_equal(expected, result)

    def test_shrink_one_point_array(self):
        array = np.array([8])

        result = nm.shrink_points(array, 0)
        expected = np.array([8])

        np.testing.assert_array_equal(expected, result)

    def test_shrink_wrong_index(self):
        array = np.array([8])
        index = -34

        expected = Exception

        self.assertRaises(expected, nm.shrink_points,
                          array, index)

    def test_make_step(self):
        simplex = np.array([[1, 0], [0, 1], [1, 1]])
        function_str = "x1^2 + x2^2"
        dimensions, function = fp.function_parsing(function_str)
        fun = lambda x: eval(function)

        result = nm.make_step(fun, simplex)
        expected = np.array([[1, 0], [0, 1], [0, 0]])

        np.testing.assert_array_equal(expected, result)

    def test_calculate_usual(self):
        function_str = "x1^2 + x2^2"
        dimensions, function = fp.function_parsing(function_str)
        fun = lambda x: eval(function)

        result = nm.calculate_neldermead(fun, dimensions)
        expected = np.array([0, 0])

        np.testing.assert_array_almost_equal(expected, result)

    def test_calculate_wrong_coefficient(self):
        function_str = "x1^2 + x2^2"
        dimensions, function = fp.function_parsing(function_str)
        fun = lambda x: eval(function)

        expected = Exception

        self.assertRaises(expected, nm.calculate_neldermead,
                          fun, dimensions, -1, -1, -1)

    def test_calculate_wrong_dimension(self):
        function_str = "x1^2 + x2^2"
        dimensions, function = fp.function_parsing(function_str)
        fun = lambda x: eval(function)

        expected = Exception

        self.assertRaises(expected, nm.calculate_neldermead,
                          fun, -1)

    def test_calculate_one_dimension(self):
        function_str = "x1^2"
        dimensions, function = fp.function_parsing(function_str)
        fun = lambda x: eval(function)

        result = nm.calculate_neldermead(fun, dimensions)
        expected = np.array([0])

        np.testing.assert_array_almost_equal(expected, result)

    def test_calculate_const(self):
        function_str = "2"
        dimensions, function = fp.function_parsing(function_str)
        fun = lambda x: eval(function)

        result = nm.calculate_neldermead(fun, dimensions)
        expected = np.array([2])

        np.testing.assert_array_almost_equal(expected, result)

    def test_calculate_infinity(self):
        function_str = "x1"
        dimensions, function = fp.function_parsing(function_str)
        fun = lambda x: eval(function)

        result = nm.calculate_neldermead(fun, dimensions)
        expected = np.array([np.nan])

        np.testing.assert_array_almost_equal(expected, result)
