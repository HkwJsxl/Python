# python创建进程

### 创建进程方法一

```python
import time
from multiprocessing import Process


def func(name):
    print(name)
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')


if __name__ == '__main__':
    pcs = Process(target=func, args=('hkw',))
    pcs.start()
    print('main')
```

### 创建进程方法二

```python
import time
from multiprocessing import Process


class MyProcess(Process):
    def run(self):
        print('hkw')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('2')


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('main')
```

### join方法

```
"""主进程等待子进程运行结束之后再继续往后执行"""
```

```python
import time
from multiprocessing import Process


def func(name, n):
    print(name)
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')


if __name__ == '__main__':
    p = Process(target=func, args=('hkw', 1,))
    p1 = Process(target=func, args=('jon', 2,))
    p2 = Process(target=func, args=('liu', 3,))
    start_time = time.time()
    p.start()
    p1.start()
    p2.start()
    p.join()
    p1.join()
    p2.join()
    print('main', time.time() - start_time)
```

```python
import time
from multiprocessing import Process


def func(name, n):
    print(name)
    time.sleep(n)
    print(f'{n}')


if __name__ == '__main__':
    for i in range(1, 4):
        p = Process(target=func, args=('hkw', i,))
        start_time = time.time()
        p.start()
        p.join()
    print('main', time.time() - start_time)
```

```python
import time
from multiprocessing import Process


def func(name, n):
    print(name)
    time.sleep(n)
    print(f'{n}')


if __name__ == '__main__':
    p_list = []
    for i in range(1, 4):
        p = Process(target=func, args=('hkw', i,))
        start_time = time.time()
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
    print('main', time.time() - start_time)
```

### 进程间相互隔离

```python
from multiprocessing import Process

name = 'jon'


def func():
    global name
    name = 'lin'
    print('func %s' % name)


if __name__ == '__main__':
    p = Process(target=func, )
    p.start()
    p.join()
    print('main %s' % name)
```

### 进程PID号

```python
"""
# 查看进程PID号
# 每次运行进程PID不同
# 终端查看进程
	tasklist |findstr PID  (win)
    ps aux|grep PID  (mac)
os.getpid()  # 当前进程PID号
os.getppid()  # 当前父进程PID号
p.terminate()  # 杀死进程
print(p.is_alive())  # 判断当前进程是否存活
"""
```

```python
import os
import time
from multiprocessing import Process, current_process


def func():
    pid = current_process().pid
    pid1 = os.getpid()
    pid2 = os.getppid()
    print('func---PID: %s' % pid)
    print('func---PID: %s' % pid1)
    print('func---PPID: %s' % pid2)
    time.sleep(10)


if __name__ == '__main__':
	p.start()
    print(p.is_alive())
    p.join()
    p.terminate()  # 告诉操作系统去杀死当前进程，但是需要一定时间
    print(p.is_alive())
    print('main---PID: %s' % os.getpid())
    print('main---PPID: %s' % os.getppid())
```

### 僵尸进程与孤儿进程

```python
"""
僵尸进程：
	死了但是没有死透
	开设子进程后，该进程死后不会立刻释放占用的进程号，以便父进程能够查看到开设的子进程的一些基本信息（占用PID号，运行时间---）
	所有的进程都会步入僵尸进程
	回收子进程占用的PID号
		父进程等待子进程运行结束
		父进程调用join方法
孤儿进程：
	子进程存活，父进程意外死亡（没有父进程帮忙回收资源）
		操作系统会开设一个专门管理孤儿进程回收相关的资源
"""
```

### 守护进程

```python
"""
共生共存

p.daemo = True

"""
```

```python

from multiprocessing import Process
import time


def func(name='Jon'):
    print('%s 存活' % name)
    time.sleep(2)
    print('%s 死亡' % name)


if __name__ == '__main__':
    # p = Process(target=func,args=('Jon',))
    p = Process(target=func, kwargs={'name': 'Lin', })
    p.daemon = True  # 必须放在start前
    p.start()
    # p.daemon = True  # AssertionError: process has already started
    p.join()  # 没有join进程p不会存活执行
    print('main')
```

### 互斥锁

```python
"""   
多个进程操作同一份数据的时候，会出现数据错乱的问题
针对上述问题，解决方式是加锁处理：
	将并发变成串行，牺牲效率，保证数据的安全性
"""
```

```python
```

