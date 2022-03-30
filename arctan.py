from math import pi
from math import fabs

def arctan(t):

 def arctan_plus(x):

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
   k = arctan_plus(t)
 else :                              #利用arctan(-x) = - arctanx
   k = -arctan_plus(-t)

 return k

u1 = (0 == arctan(0))
u2 = (30 == arctan(0.5773))
u3 = (45 == arctan(1))
u4 = (60 == arctan(1.732))
u5 = (0 == arctan(0))
u6 = (-30 == arctan(-0.5773))
u7 = (-45 == arctan(-1))
u8 = (-60 == arctan(-1.732))

if(u1 or u2 or u3 or u4 or u5 or u6 or u7 or u8):
    print('通过测试')
