"""
建立1个包含10个字符的字符串

建立1个包含10个字符的字符串，并根据键盘输入的数字n输出字符串中的第n个字符。
当n值超过字符串的索引时，自动转为输出字符串中的最后1个字符。

要求：
    用try语句实现。
"""

s = 'helloWorld'
choice = eval(input('请输入要查询的字符索引：').strip())
try:
    print(s[choice])
except Exception:
    print(s[-1])
