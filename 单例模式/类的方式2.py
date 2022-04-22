"""
IO操作耗时，并没有实现
当他们判断的时候，还没有对象完成实例化，所以就会调用init()方法进行实例化，结果就是调用了多次，然后就创建了多个对象。

"""
from threading import Thread


class Singleton(object):
    def __init__(self, *args, **kwargs):
        import time
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # hasattr() 函数用于判断对象是否包含对应的属性 , 这里是看看这个类有没有 _instance 属性
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)

        return Singleton._instance


def task():
    obj = Singleton.get_instance()
    print(obj)


for i in range(10):
    t = Thread(target=task)
    t.start()
