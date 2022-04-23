import queue

'''先进先出'''
q = queue.Queue(5)
q.put(1)
q.put(2)
q.put(3)
print(q.get())

'''后进先出'''
q = queue.LifoQueue(5)
q.put(1)
q.put(2)
q.put(3)
print(q.get())

'''优先级'''
q = queue.PriorityQueue(5)
# put中放入元组，第一个表示优先级，第二个表示内容，数字越小，优先级越高
q.put((1, '1'))
q.put((10, '2'))
q.put((100, '3'))
print(q.get())
