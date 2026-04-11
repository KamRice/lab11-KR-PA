# https://github.com/KamRice/lab11-KR-PA
# Partner 1: Kameron Rice
# Partner 2: Palmer Ackerbloom

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    pass

    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_multiply(self):  # 3 assertions
        self.assertEqual(calculator.mul(5, 5), 25)
        self.assertEqual(calculator.mul(-5, 5), -25)
        self.assertEqual(calculator.mul(0, 5), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(calculator.div(5, 0), None)
        self.assertEqual(calculator.div(10, 5), 2)
        self.assertEqual(calculator.div(-10, 5), -2)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        self.assertIsNone(calculator.logarithm(0, 5))
        self.assertIsNone(calculator.logarithm(-1, 5))

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3, 3), 4.242640687119285)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.4142135623730951)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            calculator.square_root(-2)

    ##########################

    # Do not touch this
    if __name__ == "__main__":
        unittest.main()
