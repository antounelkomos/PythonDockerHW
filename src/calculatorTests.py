import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(selfs):
        calculator = calculator()
        self.assertIsInstance(calculator, calculator)


if __name__ == '__main__':
    unittest.main()