"""
计算值
    2sin85/(1+e2)
    0.5*in(x+√1+x²)
"""
import math

z1 = (2 * (math.sin(math.pi * 85 / 180))) / (1 + math.e ** 2)
print(z1)

x = int(input('请输入整数：'))
z2 = 1 / 2 * math.log(x + math.sqrt(1 + math.pow(x, 2)))
print(z2)
