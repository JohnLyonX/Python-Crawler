import asyncio

import matplotlib.pyplot as plt


# 新版写法(推荐)

async def foo(i):
    print(f'foo{i}start')
    await asyncio.sleep(i)
    print(f'foo{i}end')
    return 1 * i


def callback(task):
    print(f"返回了{task.result()}")


loop = asyncio.get_event_loop()


# 定义一个主任务
async def mainTask():
    tasks = [
        # 作用是将协程对象包装成一个任务对象
        asyncio.ensure_future(foo(1)),
        asyncio.ensure_future(foo(2)),
        asyncio.ensure_future(foo(3))
    ]

    # 方式一
    '''
    # 给第一个任务添加回调函数
    tasks[0].add_done_callback(lambda ret: print(ret.result()))
    # 阻塞等待所有的协程结束
    await asyncio.wait(tasks)

    for task in tasks:
        print(task.done(), task.result())
    '''

    # 方式二
    '''
        * 表示不定长参数
        def func(*args):
            print(args)
        func(1,2,3,4,5,6,7,8,9)
        打印: 1, 2, 3, 4, 5, 6, 7, 8, 9
        tips: 如果需要传递一个列表, 需要在列表前面加上 *, 例如: func(*[1,2,3,4,5,6,7,8,9])
        
        传入多个参数
        def func(args, args2):
            print(args,args2)
        
        func([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]))
        打印: 1,2,3,4,5,6,7,8,9, 1,2,3,4,5,6,7,8,9
        
        **keyargs 表示不定长的关键字参数
        def func(**keyargs):
            print(keyargs)
        dic = {'a':1, 'b':2, 'c':3}
        func(dic)
        打印: {'a': 1, 'b': 2, 'c': 3}
    '''
    ret = await asyncio.gather(*tasks) # 将任务列表一起传入进去
    print(ret)


asyncio.run(mainTask())