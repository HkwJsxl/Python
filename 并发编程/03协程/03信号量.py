import random
import time
from threading import Thread, Semaphore

sm = Semaphore(5)


def func(name):
    sm.acquire()
    print('%s 正在蹲厕所！' % name)
    # time.sleep(2)
    time.sleep(random.randint(1, 3))
    sm.release()


if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=func, args=('%s号' % i,))
        t.start()
