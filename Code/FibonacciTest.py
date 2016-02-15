import unittest
from Code import Fibonacci

__author__ = 'Cindy Lehner'

class FibonacciTest(unittest.TestCase):

    def testCalculation1(self):
        self.assertEqual(Fibonacci.fib(0),0)

    def testCalculation2(self):
        self.assertEqual(Fibonacci.fib(5),5)

    def testCalculation3(self):
        self.assertEqual(Fibonacci.fib(1),5)

if __name__ == "__main__":
    unittest.main()

#Ende