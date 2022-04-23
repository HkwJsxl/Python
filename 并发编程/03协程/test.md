### 测验

-   简述死锁现象

    抢没有释放的锁时，发生阻塞现象

    ​	mutexA拿到A锁，mutexB拿到B锁

    ​	mutexA没有释放A，mutexB没有释放B的情况下，mutexB要拿A锁，mutexA要拿B锁

-   你用过哪些队列

    ```python
    import queue
    
    ​	queue.Queue()  先进先出
    
    ​	queue.LifoQueue()  后进先出
    
    ​	queue.PriorityQueue()  优先级队列，put放入元组，第一个参数表示优先级，第二个参数表示内容，优先级数字越低，优先级越高
    
    ​	from multiprocessing import Queue
    ```

    

-   阐述进程池线程池概念及基本使用

    池：在保证计算机硬件的安全下，最大限度的去利用硬件资源

    ​	因为硬件的开发速度是比不上软件的，而且资源也是有限的

    ​	池的出现实际上是保证了计算机硬件的安全，降低了它的开发效率

    基于多进程或多线程实现的并发套接字通信，有个致命缺陷：

    ​	服务器运行在一台主机上，主机所能承受的压力是一定的，性能是有限的，不能无限的开线程

    ​	服务的开启的进程数或线程数会随着客户端的数目增多而增多，这会给服务器主机带来一定压力，当达到一个结点时，服务器可能会奔溃，这就有了池的概念，给服务端的进程或线程数目进行一个合理的控制，以保证服务器主机不会奔溃

    基本使用：

​		

```python
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
pool = ThreadPoolExecutor()

pool = ProcessPoolExecutor()
pool.submit(task, i).add_done_callback(call_back)

"""
```



-   什么是协程，如何简单实现

协程是单线程当中实现的并发，相对于开多个线程实现并发，省去了多个线程之间切换的开销，运行效率得到了提高

协程的作用是在执行函数A时随时可以去执行函数B，然后终端函数B去执行函数A（连续的自由切换）

协程优势：

-   执行效率极高，因为子程序切换（函数）不是线程切换，由程序自身控制，没有切换线程的开销。所以与多线程相比，线程的数量越多，协程性能的优势越明显。
-   不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在控制共享资源时也不需要加锁，因此执行效率高很多。

```python
from gevent import spawn
from gevent import monkey

monkey.patch_all()
# 猴子补丁
```

