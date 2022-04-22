"""

改进：
    让__init__方法仅执行一次

"""


class Singleton(object):

    def __init__(self):
        if not hasattr(Singleton, "_first_init"):
            print("__init__")
            Singleton._first_init = True

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if not hasattr(Singleton, "_instance"):
            print("创建新实例")
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)
