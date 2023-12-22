import multiprocessing
import time


def foo():
    print('执行foo')
    print('结束执行foo')


if __name__ == '__main__':
    for i in range(5):
        # 并发执行
        t1 = multiprocessing.Process(target=foo)  # 创建进程
        t1.start()
