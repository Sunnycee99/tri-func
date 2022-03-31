from math import fabs
from math import pi
import math
import random


def arcsin(x):
    """
    The implementation of arcsin function.

    Args:
        x: input value (should be within the range of -1 to 1 ) to be calculated.

    Returns:
        The radian result of the arcsin calculation.
    """

    if not (-1 <= x <= 1):
        return False
    elif fabs(x) == 1:
        return x * 90
    else:
        g = x
        t = x
        n = 1
        while fabs(t) >= 1e-16:
            t = t * (2 * n - 1) * (2 * n - 1) * x * x / ((2 * n) * (2 * n + 1))
            n += 1
            g += t

        return round(g * 180 / pi, 4)


def arcsinTest():
    """
    Function used to test arcsin().

    Returns:
        None
    """

    for i in range(50):
        x = random.random()
        y = -random.random()

        assert fabs(arcsin(x) - math.asin(x) * 180 / pi) <= 1e-4, 'error within arcsin function!'
        assert fabs(arcsin(y) - math.asin(y) * 180 / pi) <= 1e-4, 'error within arcsin function!'
    assert fabs(arcsin(1) - math.asin(1) * 180 / pi) <= 1e-4, 'error within arcsin function!'
    assert fabs(arcsin(-1) - math.asin(-1) * 180 / pi) <= 1e-4, 'error within arcsin function!'
    print('arcsin function with correct input was tested successfully.')
    print('the following False comes from arcsin function with input out of domain')

    x = random.randint(2, 10)
    print(arcsin(x))


arcsinTest()
