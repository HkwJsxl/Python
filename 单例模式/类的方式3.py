"""
方式二 加锁
    得到的都是同一对象
"""
from threading import Thread, Lock


class Singleton(object):
    _instance_lock = Lock()  # 线程锁

    def __init__(self, *args, **kwargs):
        import time
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        with Singleton._instance_lock:
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
