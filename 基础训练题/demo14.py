"""
数字加密游戏

    编程程序，从键盘任意输入1个4位数，将该数字中的每位数与7相乘，然后取乘积结果的个位数对该数字进行替换，最后得到1个新的4位数。


"""
# while True:
#     num = input('请输入一个四位数：').strip()
#     if len(num) != 4 or not num.isdigit():
#         print('四位数啊！')
#         continue
#     last = ''
#     for x in range(len(num)):
#         y = int(num[x]) * 7 % 10
#         print(y)
#         y = str(y)
#         last += y
#     print(last)
#     break

try:
    n = int(input('任意输入1个4位数:').strip())
    if 1000 <= n <= 9999:
        a = n % 10
        b = (n - a) % 100 / 10
        c = (n - a - 10 * b) % 1000 / 100
        d = (n - a - 10 * b - 100 * c) % 10000 / 1000
        a = a * 7 % 10
        b = b * 7 % 10
        c = c * 7 % 10
        d = d * 7 % 10
        n = 1000 * d + 100 * c + 10 * b + a
        print(int(n))
    elif n <= 1000 or n >= 9999:
        print("您输入的数字不符合要求，请输入一个四位数字")
except Exception as e:
    print(e)
