import unittest
from method.nelder_mead import calculate_neldermead


class Test(unittest.TestCase):
    def test_usual(self):
        func = "x[0]**2 + (x[1] - 6)**2"
        n = 2
        f = lambda x: eval(func)
        points = calculate_neldermead(f, n)
        self.assertEqual(points[0], 0)
        self.assertEqual(points[1], 6)
    def test_zeros(self):
        func = "x[0]**2 + x[1]**2"
        n = 2
        f = lambda x: eval(func)
        points = calculate_neldermead(f, n)
        self.assertEqual(points.all(), 0)

    def test_one_dim(self):
        func = "x[0]**2"
        n = 2
        f = lambda x: eval(func)
        points = calculate_neldermead(f, n)
        self.assertEqual(points.all(), 0)
