"""

当python实例化一个对象时，是先执行类的__new__()方法，
当我们没写__new__()方法时，
默认调用基类object的__new__()方法，然后再执行类的__init__()方法，
对这个对象进行初始化，所有我们可以基于这个，去实现单例模式

"""


class Singleton(object):

    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if not hasattr(Singleton, "_instance"):
            print(" 创建新实例 ")
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)
