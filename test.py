import unittest

import main
import methods


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.func1 = main.func1
        self.func2 = main.func2

    def test_func1(self):
        self.assertAlmostEqual(self.func1(-5.0), 0.642857142857142)
        self.assertAlmostEqual(self.func1(-4.0), 0.615384615384615)
        self.assertAlmostEqual(self.func1(-3.0), 0.583333333333333)
        self.assertAlmostEqual(self.func1(-2.0), 0.545454545454545)
        self.assertEqual(self.func1(-1.0), 0.5)
        self.assertAlmostEqual(self.func1(0.0), 0.444444444444444)
        self.assertEqual(self.func1(1.0), 0.375)
        self.assertAlmostEqual(self.func1(2.0), 0.285714285714285)
        self.assertAlmostEqual(self.func1(3.0), 0.166666666666666)
        self.assertEqual(self.func1(4.0), 0.0)
        self.assertEqual(self.func1(5.0), -0.25)

    def test_func2(self):
        self.assertEqual(self.func2(-2.0), 3)
        self.assertEqual(self.func2(-1.5), 1.25)
        self.assertEqual(self.func2(-1.0), 0)
        self.assertEqual(self.func2(-0.5), 0.75)
        self.assertEqual(self.func2(0.0), 1)
        self.assertEqual(self.func2(0.5), 0.75)
        self.assertEqual(self.func2(1.0), 0)
        self.assertEqual(self.func2(1.5), 1.25)
        self.assertEqual(self.func2(2.0), 3)


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.dichot = methods.dichotomic_search
        self.fib = methods.fibonacci_of
        self.fib_seq = methods.fibonacci_seq

    # TODO: тесты для дихотомического поиска
    def test_dichot(self):
        self.assertAlmostEqual(
            first=self.dichot(
                lambda x: x*x + 2 * x,
                a=-3, b=5, eps=0.05, l=0.2
            )[0],
            second=-1.0,
            delta=0.1
        )

    def test_fib(self):
        self.assertEqual(self.fib(0), 0)
        self.assertEqual(self.fib(1), 1)
        self.assertEqual(self.fib(2), 1)
        self.assertEqual(self.fib(3), 2)
        self.assertEqual(self.fib(4), 3)
        self.assertEqual(self.fib(5), 5)
        self.assertEqual(self.fib(6), 8)
        self.assertEqual(self.fib(7), 13)
        self.assertEqual(self.fib(8), 21)
        self.assertEqual(self.fib(9), 34)
        self.assertEqual(self.fib(10), 55)
        self.assertEqual(self.fib(19), 4181)
        self.assertEqual(self.fib(100), 354224848179261915075)

    def test_fib_seq(self):
        self.assertEqual(
            self.fib_seq(10),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        )


if __name__ == "__main__":
    unittest.main()
