from math import pi
from math import fabs

def atan(t):

 def atan_plus(x):

    if fabs(x) < 1:                 # 输入值绝对值小于1时，采用泰勒级数展开
        g = x
        for i in range(1, 10000):
            t = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
            g += t

    else:                           # 输入值绝对值大于1，利用arctan(1/x) = pi/2 - arctan(x)
        x = 1 / x
        g = x
        for i in range(1, 10000):
            t = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
            g += t
        g = pi / 2 - g

    d = round(g / pi * 180, 2)  #完成弧度到角度的变换，同时四舍五入保留两位小数
    return d

 if t > 0:
   k = atan_plus(t)
 else :                              #利用arctan(-x) = - arctanx
   k = -atan_plus(-t)

 return k

u1 = (0 == atan(0))
u2 = (30 == atan(0.5773))
u3 = (45 == atan(1))
u4 = (60 == atan(1.732))
u5 = (0 == atan(0))
u6 = (-30 == atan(-0.5773))
u7 = (-45 == atan(-1))
u8 = (-60 == atan(-1.732))

if(u1 and u2 and u3 and u4 and u5 and u6 and u7 and u8):
    print('通过测试')
else:
    print('未通过测试')
