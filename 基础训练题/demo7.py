"""

编写函数
该函数可以输入任意多个数，函数返回输出所有输入参数的最大值、最小值和平均值。


"""

"""
def func(lst):
    max = lst[0]
    min = lst[0]
    s = 0
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < max:
            min = lst[i]
        s += eval(lst[i])
    average = s / len(lst)
    print(max)
    print(min)
    print(average)


lst = list(input('请输入一组数，并用空格隔开：').strip().split(' '))
func(lst)
"""

import numpy as py

x = input('请输入一组数并用空格隔开：').strip()


def f(x):
    lst = list(x.split(' '))
    for i in range(len(lst)):
        lst[i] = eval(lst[i])
    print('该组数值的最大值为：', max(lst))
    print('该组数值的最小值为：', min(lst))
    print('该组数值的平均值为：', py.mean(lst))


f(x)
