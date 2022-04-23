import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

pool = ThreadPoolExecutor(max_workers=10)  # 10个线程
    

def task(n):
    print(n)
    time.sleep(2)
    return '>>>%s' % n


"""
池子造出来之后 里面会固定存在十个线程
这个十个线程不会出现重复创建和销毁的过程

提交任务的方式：
    同步：提交任务之后原地等待任务的返回结果 期间不做任何事
    异步：提交任务之后不等待任务的返回结果 执行继续往下执行
"""

lst = []
for i in range(20):
    res = pool.submit(task, i)  # 提交任务，异步提交
    # print(res.result())  # result() 变为同步，返回值为 任务的返回值
    lst.append(res)
pool.shutdown()  # 关闭线程池，等待线程池中所有任务运行完毕，result任务返回值同时打印
for li in lst:
    print(li.result())  # 异步，有序的
