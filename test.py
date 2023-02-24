import unittest

import main


class TestDichotomic(unittest.TestCase):
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

    # TODO: тесты для дихотомического поиска


if __name__ == "__main__":
    unittest.main()
