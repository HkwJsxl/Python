"""
从键盘输入一个1~7的数字，格式化输出对应数字的星期字符串名称。如：输入3，返回“您输入的是星期三”。

"""

from datetime import datetime

n = int(input('输入一个1~7的数字:'))
if (n == 1):
    print("您输入的是星期一")
elif (n == 2):
    print("您输入的是星期二")
elif (n == 3):
    print("您输入的是星期三")
elif (n == 4):
    print("您输入的是星期四")
elif (n == 5):
    print("您输入的是星期五")
elif (n == 6):
    print("您输入的是星期六")
elif (n == 7):
    print("您输入的是星期日")

print("0表示周一,2表示周二,...,6表示周日")
print(datetime.today().weekday())
