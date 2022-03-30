from math import fabs
from math import pi
import math
import random


def cos(x, radian_mode=False):
    """
    The implementation of cos function.

    Args:
        x: input value to be calculated, either angle or radian.
        radian_mode: boolean value used to switch mode.

    Returns:
        The result of the cos calculation.
    """

    if not radian_mode:
        x = x * pi / 180

    x = x % (2 * pi)
    g = 1
    t = - x * x / 2
    n = 1

    while fabs(t) >= 1e-16:
        g += t
        n += 1
        t = -t * x * x / (2 * n) / (2 * n - 1)

    return round(g, 4)


def cosTest():
    """
    Function used to test cos().

    Returns:
        None
    """

    for i in range(50):
        x = 5 * pi * random.random()
        y = - 5 * pi * random.random()

        assert fabs(cos(x * 180 / pi) - math.cos(x)) <= 1e-4, 'error within cos function!'
        assert fabs(cos(x, radian_mode=True) - math.cos(x)) <= 1e-4, 'error within cos function!'
        assert fabs(cos(y * 180 / pi) - math.cos(y)) <= 1e-4, 'error within cos function!'
        assert fabs(cos(y, radian_mode=True) - math.cos(y)) <= 1e-4, 'error within cos function!'

    print('cos function was tested successfully.')


cosTest()
