"""
猜数游戏

首先由计算机产生一个[1,100]之间的随机整数，然后由用户猜测所产生的随机数。
根据用户猜测的情况给出不同提示，如猜测的数大于产生的数，则显示“High”，小于则显示“Low”，等于则显示“You won !”，游戏结束。
用户最多可以猜7次，如果7次均未猜中，则显示“You lost !”，并给出正确答案，游戏结束。
游戏结束后，询问用户是否继续游戏，选择“Y”则开始一轮新的猜数游戏；选择“N”则退出游戏。

"""
import random

while True:
    random_num = random.randint(1, 100)
    for i in range(1, 8):
        num = eval(input(f'请输入您第{i}次猜的数：').strip())
        if num > random_num:
            print('High')
        elif num < random_num:
            print('Low')
        else:
            print('You win !')
            break
        if i == 7:
            print('You lost !')
    con = input('是否继续y / other：').strip()
    if con.lower() == 'y':
        continue
    else:
        break
