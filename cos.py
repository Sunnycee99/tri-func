import math
import unittest
import random

def factorial(a):  

  """
  实现阶乘计算

  输入：
     a：为需要进行阶乘计算的值
  返回：
     阶乘计算的结果
  """
  b=1
  while a!=1:
    b*=a
    a-=1
  return b
  
def taylor(x,model):
  """
  进行泰勒级数展开式计算

  输入：
     x：需要计算的角度或弧度
     model：计算模式，角度计算过着弧度计算，默认为角度计算
  返回：
     计算的结果
  """
  a=1
  n=50
  if model:
    x=x  
  else:
    x = x/180*(math.pi)   # 转换为弧度
  count=1
  for k in range(1,n):
    if count%2!=0:
      a-=(x**(2*k))/factorial(2*k)
    else:
      a+=(x**(2*k))/factorial(2*k)
    count+=1
  return a
  
def cos(x,model=False):
   """
   定义cos计算接口

   输入：
     x：需要计算的角度或弧度
     model：计算模式，角度计算过着弧度计算，默认为角度计算
   返回：
     计算的结果，保留3位小数
   """
   return round(taylor(x,model),3)


def cos_test():
    """
    对cos函数进行测试

    """
    num=0
    for i in range(100):
        #print('第',i,'次实验：')
        x=random.uniform(0, 1000)
        #print(x)
        x1=cos(x)
        #print(x1)

        x2 = x / 180 * (math.pi)  # 转换为弧度
        x2=math.cos(x2)
        x2=round(x2,3)
        #print(x2)
        if x1==x2:
            num=num+1
        #print('-------------')

    per=round(num/100*100,2)
    print('角度计算准确率为：',per,'%')

    '''
    弧度计算准确率测试
    '''
    num=0
    for i in range(100):
        #print('第',i,'次实验：')
        x=random.uniform(0, 10)
        x=x*math.pi
        #print(x)
        x1=cos(x,True)
        #print(x1)
        x2=math.cos(x)
        x2=round(x2,3)
        #print(x2)
        if x1==x2:
            num=num+1
        #print('-------------')

    #print(cos(314,True))
    #print(round(math.cos(314),3))
    #per=round(num/100*100,2)
    print('弧度计算准确率为：',per,'%')



cos_test()
