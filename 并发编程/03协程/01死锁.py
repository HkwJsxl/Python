import time
from threading import Thread, Lock

mutexA = Lock()
mutexB = Lock()


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('%s 抢到A锁' % self.name)  # 获取当前线程名
        mutexB.acquire()
        print('%s 抢到B锁' % self.name)
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('%s 抢到B锁' % self.name)
        time.sleep(1)
        mutexA.acquire()  # 线程1再抢A时，A被下一个线程占用
        print('%s 抢到A锁' % self.name)
        mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
