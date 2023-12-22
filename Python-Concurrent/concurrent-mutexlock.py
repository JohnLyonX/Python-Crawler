import threading
import time

import requests
from lxml import etree

x = 100
lock = threading.Lock()
lock.acquire()  # 加锁
lock.release()  # 加锁


def foo():
    global x
    temp = x - 1
    time.sleep(1)  # 当线程执行到这里之后,会休眠,接着其他线程又会取得CPU的使用权,导致结果是错误的
    x = temp
    print(x)


for i in range(99):
    t = threading.Thread(target=foo)
    t.start()


# 解决方法,使用互斥锁

def bar():
    lock.acquire()
    global x
    temp = x - 1
    time.sleep(1)  # 当线程执行到这里之后,会休眠,接着其他线程又会取得CPU的使用权,导致结果是错误的\
    x = temp
    print(x)
    lock.release()


for i in range(99):
    t = threading.Thread(target=bar)
    t.start()