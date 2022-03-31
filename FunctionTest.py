import unittest
from math import pi
from arcsin import arcsin
from arctan import arctan
from sin import sin
from cos import cos


class TestFunc(unittest.TestCase):         # 测试类

    def test_arcsin(self):                 # 测试arcsin函数
        self.assertEqual(0, arcsin(0))
        self.assertEqual(30, arcsin(0.5))
        self.assertEqual(45, arcsin(0.707107))
        self.assertEqual(60, arcsin(0.866025))
        self.assertEqual(90, arcsin(1))
        self.assertEqual(-30, arcsin(-0.5))
        self.assertEqual(-45, arcsin(-0.707107))
        self.assertEqual(-90, arcsin(-1))
        self.assertEqual(-60, arcsin(-0.866025))

    def test_arctan(self):                 # 测试arctan函数
        self.assertEqual(0, arctan(0))
        self.assertEqual(30, arctan(0.5773))
        self.assertEqual(45, arctan(1))
        self.assertEqual(60, arctan(1.732))
        self.assertEqual(0, arctan(0))
        self.assertEqual(-30, arctan(-0.5773))
        self.assertEqual(-45, arctan(-1))
        self.assertEqual(-60, arctan(-1.732))

    def test_cos(self):                    # 测试cos函数
        self.assertEqual(1, cos(0))
        self.assertEqual(0.866, cos(30))
        self.assertEqual(0.5, cos(60))
        self.assertEqual(0, cos(90))
        self.assertEqual(-0.5, cos(120))
        self.assertEqual(-1, cos(180))
        self.assertEqual(0, cos(270))
        self.assertEqual(1, cos(360))
        self.assertEqual(0.866, cos(-30))
        self.assertEqual(0.5, cos(-60))
        self.assertEqual(0, cos(-90))
        self.assertEqual(-0.5, cos(-120))
        self.assertEqual(-1, cos(-180))
        self.assertEqual(0, cos(-270))
        self.assertEqual(1, cos(-360))
        self.assertEqual(1, cos(0, True))
        self.assertEqual(0.866, cos(30/180 * pi, True))
        self.assertEqual(0.5, cos(60/180 * pi, True))
        self.assertEqual(0, cos(90/180 * pi, True))
        self.assertEqual(-0.5, cos(120/180 * pi, True))
        self.assertEqual(-1, cos(180/180 * pi, True))
        self.assertEqual(0, cos(270/180 * pi, True))
        self.assertEqual(1, cos(360/180 * pi, True))
        self.assertEqual(0.866, cos(-30/180 * pi, True))
        self.assertEqual(0.5, cos(-60/180 * pi, True))
        self.assertEqual(0, cos(-90/180 * pi, True))
        self.assertEqual(-0.5, cos(-120/180 * pi, True))
        self.assertEqual(-1, cos(-180/180 * pi, True))
        self.assertEqual(0, cos(-270/180 * pi, True))
        self.assertEqual(1, cos(-360/180 * pi, True))

    def test_sin(self):                    # 测试sin函数
        self.assertEqual(0, sin(0))
        self.assertEqual(0.5, sin(30))
        self.assertEqual(0.866, sin(60))
        self.assertEqual(1, sin(90))
        self.assertEqual(0.866, sin(120))
        self.assertEqual(0, sin(180))
        self.assertEqual(-1, sin(270))
        self.assertEqual(0, sin(360))
        self.assertEqual(-0.5, sin(-30))
        self.assertEqual(-0.866, sin(-60))
        self.assertEqual(-1, sin(-90))
        self.assertEqual(-0.866, sin(-120))
        self.assertEqual(0, sin(-180))
        self.assertEqual(1, sin(-270))
        self.assertEqual(0, sin(-360))
        self.assertEqual(0, sin(0))
        self.assertEqual(0.5, sin(30/180 * pi, True))
        self.assertEqual(0.866, sin(60/180 * pi, True))
        self.assertEqual(1, sin(90/180 * pi, True))
        self.assertEqual(0.866, sin(120/180 * pi, True))
        self.assertEqual(0, sin(180/180 * pi, True))
        self.assertEqual(-1, sin(270/180 * pi, True))
        self.assertEqual(0, sin(360/180 * pi, True))
        self.assertEqual(-0.5, sin(-30/180 * pi, True))
        self.assertEqual(-0.866, sin(-60/180 * pi, True))
        self.assertEqual(-1, sin(-90/180 * pi, True))
        self.assertEqual(-0.866, sin(-120/180 * pi, True))
        self.assertEqual(0, sin(-180/180 * pi, True))
        self.assertEqual(1, sin(-270/180 * pi, True))
        self.assertEqual(0, sin(-360/180 * pi, True))

if __name__ == '__main__':
    unittest.main()


