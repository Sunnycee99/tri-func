from math import fabs
from math import pi
import math
import random


def sin(x, radian_mode=False):
    """
    The implementation of sin function.

    Args:
        x: input value to be calculated, either angle or radian.
        radian_mode: boolean value used to switch mode.

    Returns:
        The result of the sin calculation.
    """

    if not radian_mode:
        x = x * pi / 180

    x = x % (2 * pi)
    g = 0
    t = x
    n = 1

    while fabs(t) >= 1e-16:
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)

    return round(g, 4)


def sinTest():
    """
    Function used to test sin().

    Returns:
        None
    """

    for i in range(50):
        x = 5 * pi * random.random()
        y = - 5 * pi * random.random()

        assert fabs(sin(x * 180 / pi) - math.sin(x)) <= 1e-4, 'error within sin function!'
        assert fabs(sin(x, radian_mode=True) - math.sin(x)) <= 1e-4, 'error within sin function!'
        assert fabs(sin(y * 180 / pi) - math.sin(y)) <= 1e-4, 'error within sin function!'
        assert fabs(sin(y, radian_mode=True) - math.sin(y)) <= 1e-4, 'error within sin function!'

    print('sin function was tested successfully.')


sinTest()
