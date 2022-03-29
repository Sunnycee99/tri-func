from math import fabs
from math import pi
import math
import random


def arcsin(x):
    """
    The implementation of arcsin function.

    Args:
        x: input radian value to be calculated.

    Returns:
        The radian result of the arcsin calculation.
    """

    if not (-1 <= x <= 1):
        raise RuntimeError('input out of domain!')
    else:
        g = x
        t = x
        n = 1
        while fabs(t) >= 1e-16:  # 采用泰勒级数展开进行计算逼近函数值
            t = t * (2 * n - 1) * (2 * n - 1) * x * x / ((2 * n) * (2 * n + 1))
            n += 1
            g += t

        return round(g, 4)


def arcsinTest():
    """
    Function used to test arcsin().

    Returns:
        None
    """

    for i in range(50):
        x = random.random()
        y = -random.random()

        assert fabs(arcsin(x) - math.asin(x)) <= 1e-4, 'error within arcsin function!'
        assert fabs(arcsin(y) - math.asin(y)) <= 1e-4, 'error within arcsin function!'

    print('arcsin function with correct input was tested successfully.')
    print('the following error comes from arcsin function with input out od domain')

    x = random.randint(2, 10)
    arcsin(x)


arcsinTest()
