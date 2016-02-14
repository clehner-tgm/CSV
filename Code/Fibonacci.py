import doctest

__author__ = 'Cindy Lehner'

def fib(n):

    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    doctest.testmod()