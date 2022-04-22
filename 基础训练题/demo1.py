"""
要求输出成绩等级A、B、C、D、E，其中90~100分为A，80~89分为B，70~79分为C，60~69分为D，60分以下为E。



要求：

用if语句实现；

输入百分制成绩后要判断该成绩的合理性，对不合理的成绩应输出出错信息。

"""


def level(score):
    if score < 0 or score > 100 or score % 1 != 0:
        return '输入不合法！'
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'


score = eval(input('score>>> ').strip())
print(level(score))
