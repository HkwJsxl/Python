import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

pool = ProcessPoolExecutor()


def task(n):
    print(n)
    time.sleep(2)
    return '>>>%s' % n


def call_back(res):
    print('call_back: %s' % res.result())


"""
池子造出来之后，线程不会出现重复创建和销毁的过程

提交任务的方式：
    同步：提交任务之后原地等待任务的返回结果 期间不做任何事
    异步：提交任务之后不等待任务的返回结果 执行继续往下执行
"""

# 进程必须卸载main下运行
# 报错    concurrent.futures.process.BrokenProcessPool:
# A process in the process pool was terminated abruptly while the future was running or pending.

if __name__ == '__main__':

    lst = []
    for i in range(20):
        pool.submit(task, i).add_done_callback(call_back)  # 提交任务，异步提交
        # 把pool.submit(task, i)返回值交给call_back
        # pool.submit(task, i).add_done_callback(call_back)没有返回值
        
        # res = pool.submit(task, i)  # 提交任务，异步提交
        # print(res.result())  # result() 变为同步，返回值为 任务的返回值
        # lst.append(res)
    # pool.shutdown()  # 关闭线程池，等待线程池中所有任务运行完毕，result任务返回值同时打印
    # for li in lst:
    #     print(li.result())  # 异步，有序的
