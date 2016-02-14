import unittest
from Code import Fibonacci

__author__ = 'Cindy Lehner'

class FibonacciTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(Fibonacci.fib(0),0)
        self.assertEqual(Fibonacci.fib(5),5)

if __name__ == "__main__":
    unittest.main()