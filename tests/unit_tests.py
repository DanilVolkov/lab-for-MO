import unittest

from method.nelder_mead import calculate_neldermead


class Test(unittest.TestCase):
    def test_usual(self):
        function_str = "x[0]**2 + (x[1] - 6)**2"
        dimensions = 2
        f = lambda x: eval(function_str)
        points = calculate_neldermead(f, dimensions)
        self.assertEqual(points[0], 0)
        self.assertEqual(points[1], 6)

    def test_zeros(self):
        function_str = "x[0]**2 + x[1]**2"
        dimensions = 2
        f = lambda x: eval(function_str)
        points = calculate_neldermead(f, dimensions)
        self.assertEqual(points.all(), 0)

    def test_one_dim(self):
        function_str = "x[0]**2"
        dimensions = 2
        f = lambda x: eval(function_str)
        points = calculate_neldermead(f, dimensions)
        self.assertEqual(points.all(), 0)
