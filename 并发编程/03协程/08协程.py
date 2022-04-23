import time
from gevent import spawn
from gevent import monkey

monkey.patch_all()
"""

连续IO操作

"""


def heng():
    time.sleep(1)


def ji():
    time.sleep(2)


def hahaha():
    time.sleep(3)


if __name__ == '__main__':
    start_time = time.time()
    # 3s
    g1 = spawn(heng)
    g2 = spawn(ji)
    g3 = spawn(hahaha)
    g1.join()
    g2.join()
    g3.join()
    # 6s
    # g1 = spawn(heng).join()
    # g2 = spawn(ji).join()
    # g3 = spawn(hahaha).join()
    end_time = time.time()
    print(end_time - start_time)
