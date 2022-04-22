"""
篮球比赛是高分的比赛，领先优势可能很快被反超。
作为观众，希望能在球赛即将结束时，就提早知道领先是否不可超越。
体育作家Bill James发明了一种算法，用于判断领先是否“安全”。

算法描述：

获取领先的分数 ，减去3分；
如果目前是领先队控球，则加0.5；否则减0.5（数字小于0则变成0）；
计算平方后的结果；
如果得到的结果比当前比赛剩余时间的秒数大，则领先是“安全”的。
请编写程序实现上述算法的功能，并给出运行结果。

"""

grade = eval(input('请输入领先分数:').strip())
time = eval(input('请输入剩余时间:').strip())
grade -= 3
while True:
    lead = input('是否为领先队y or n: ').strip()
    if lead.lower() == 'y':
        grade += 0.5
        break
    elif lead.lower() == 'n':
        grade -= 0.5
        break
    else:
        print('输入错误！')
if grade < 0:
    grade = 0
grade = grade * grade
if grade > time:
    print('领先是安全的')
else:
    print('有可能反超哦')
