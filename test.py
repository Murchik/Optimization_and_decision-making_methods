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
        self.golden = methods.golden_search
        self.dichot = methods.dichotomic_search
        self.fibonacci = methods.fibonacci_search
        self.fib = methods.fibonacci_of
        self.fib_seq = methods.fibonacci_seq

    def test_dichot(self):
        self.assertAlmostEqual(
            first=self.dichot(
                lambda x: x*x + 2 * x,
                a=-3, b=5, eps=0.05, l=0.2
            )[0],
            second=-1.0,
            delta=0.2
        )

        self.assertAlmostEqual(
            first=self.dichot(
                main.func1,
                a=-3, b=0, eps=0.01, l=0.1
            )[0],
            second=0.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func1,
                a=-3, b=0, eps=0.001, l=0.01
            )[0],
            second=0.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func1,
                a=-3, b=0, eps=0.0001, l=0.001
            )[0],
            second=0.0,
            delta=0.001
        )

        self.assertAlmostEqual(
            first=self.dichot(
                main.func1,
                a=0, b=3, eps=0.01, l=0.1
            )[0],
            second=3.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func1,
                a=0, b=3, eps=0.001, l=0.01
            )[0],
            second=3.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func1,
                a=0, b=3, eps=0.0001, l=0.001
            )[0],
            second=3.0,
            delta=0.001
        )

        self.assertAlmostEqual(
            first=self.dichot(
                main.func2,
                a=-3, b=0, eps=0.01, l=0.1
            )[0],
            second=-1.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func2,
                a=-3, b=0, eps=0.001, l=0.01
            )[0],
            second=-1.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func2,
                a=-3, b=0, eps=0.0001, l=0.001
            )[0],
            second=-1.0,
            delta=0.001
        )

        self.assertAlmostEqual(
            first=self.dichot(
                main.func2,
                a=0, b=3, eps=0.01, l=0.1
            )[0],
            second=1.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func2,
                a=0, b=3, eps=0.001, l=0.01
            )[0],
            second=1.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.dichot(
                main.func2,
                a=0, b=3, eps=0.0001, l=0.001
            )[0],
            second=1.0,
            delta=0.001
        )

    def test_golden(self):
        self.assertAlmostEqual(
            first=self.golden(
                lambda x: x*x + 2 * x,
                a=-3, b=5, eps=0.05, l=0.2
            )[0],
            second=-1.0,
            delta=0.2
        )

        self.assertAlmostEqual(
            first=self.golden(
                main.func1,
                a=-3, b=0, eps=0.01, l=0.1
            )[0],
            second=0.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.golden(
                main.func1,
                a=-3, b=0, eps=0.001, l=0.01
            )[0],
            second=0.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.golden(
                main.func1,
                a=-3, b=0, eps=0.0001, l=0.001
            )[0],
            second=0.0,
            delta=0.001
        )

        self.assertAlmostEqual(
            first=self.golden(
                main.func2,
                a=-3, b=0, eps=0.01, l=0.1
            )[0],
            second=-1.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.golden(
                main.func2,
                a=-3, b=0, eps=0.001, l=0.01
            )[0],
            second=-1.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.golden(
                main.func2,
                a=-3, b=0, eps=0.0001, l=0.001
            )[0],
            second=-1.0,
            delta=0.001
        )

        self.assertAlmostEqual(
            first=self.golden(
                main.func2,
                a=0, b=3, eps=0.01, l=0.1
            )[0],
            second=1.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.golden(
                main.func2,
                a=0, b=3, eps=0.001, l=0.01
            )[0],
            second=1.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.golden(
                main.func2,
                a=0, b=3, eps=0.0001, l=0.001
            )[0],
            second=1.0,
            delta=0.001
        )

    def test_fibonacci(self):
        self.assertAlmostEqual(
            first=self.fibonacci(
                lambda x: x*x + 2 * x,
                a=-3, b=5, eps=0.05, l=0.2
            )[0],
            second=-1.0,
            delta=0.2
        )

        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func1,
                a=-3, b=0, eps=0.01, l=0.1
            )[0],
            second=0.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func1,
                a=-3, b=0, eps=0.001, l=0.01
            )[0],
            second=0.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func1,
                a=-3, b=0, eps=0.0001, l=0.001
            )[0],
            second=0.0,
            delta=0.001
        )

        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func2,
                a=-3, b=0, eps=0.01, l=0.1
            )[0],
            second=-1.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func2,
                a=-3, b=0, eps=0.001, l=0.01
            )[0],
            second=-1.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func2,
                a=-3, b=0, eps=0.0001, l=0.001
            )[0],
            second=-1.0,
            delta=0.001
        )

        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func2,
                a=0, b=3, eps=0.01, l=0.1
            )[0],
            second=1.0,
            delta=0.1
        )
        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func2,
                a=0, b=3, eps=0.001, l=0.01
            )[0],
            second=1.0,
            delta=0.01
        )
        self.assertAlmostEqual(
            first=self.fibonacci(
                main.func2,
                a=0, b=3, eps=0.0001, l=0.001
            )[0],
            second=1.0,
            delta=0.001
        )

    def test_fib(self):
        self.assertEqual(self.fib(0), 1)
        self.assertEqual(self.fib(1), 1)
        self.assertEqual(self.fib(2), 2)
        self.assertEqual(self.fib(3), 3)
        self.assertEqual(self.fib(4), 5)
        self.assertEqual(self.fib(5), 8)
        self.assertEqual(self.fib(6), 13)
        self.assertEqual(self.fib(7), 21)
        self.assertEqual(self.fib(8), 34)
        self.assertEqual(self.fib(9), 55)
        self.assertEqual(self.fib(18), 4181)
        self.assertEqual(
            self.fib(99), 354224848179261915075
        )
        self.assertEqual(
            self.fib(199), 280571172992510140037611932413038677189525
        )

    def test_fib_seq(self):
        self.assertEqual(
            self.fib_seq(9),
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        )


if __name__ == "__main__":
    unittest.main()
