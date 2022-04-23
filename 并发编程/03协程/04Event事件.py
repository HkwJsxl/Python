import time
from threading import Thread, Event

event = Event()


def light():
    print('红灯等待！')
    time.sleep(3)
    print('绿灯了！')
    event.set()


def car(name):
    print('car%s 正在等红灯' % name)
    event.wait()
    print('car%s 绿灯通行' % name)


if __name__ == '__main__':
    t = Thread(target=light)
    t.start()

    for i in range(10):
        t = Thread(target=car, args=('%s' % i,))
        t.start()
