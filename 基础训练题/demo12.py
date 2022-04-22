"""

分别格式化输出0.002178对应的科学表示法形式、具有4位小数精度的浮点数形式和百分数形式，并将输出宽度设定为10、居中对齐、星号*填充。


"""

x = 0.002178
print("x对应的科学表示法形式为:", ("%e" % x).center(10, '*'))
print('x具有4位小数精度的浮点数形式为：', ('{0:.4f}'.format(x)).center(10, '*'))
print('x百分数形式为:', (('{0:.2f}%'.format(x * 100)).center(10, '*')))
