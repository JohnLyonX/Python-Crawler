import asyncio
import time


# 旧版异步实现

# 定义一个协程
async def foo(i):
    print(f'foo{i}start')
    await asyncio.sleep(i)
    print(f'foo{i}end')


# 创建事件循环对象
loop = asyncio.get_event_loop()
tasks = [
    foo(1),
    foo(2),
    foo(3)
]  # foo为协程对象
# 阻塞等待所有的协程结束
loop.run_until_complete(asyncio.wait(tasks))


# 对任务进行封装
async def foo(i):
    print(f'foo{i}start')
    await asyncio.sleep(i)
    print(f'foo{i}end')
    return 1 * i


def callback(task):
    print(task.result())


loop = asyncio.get_event_loop()
# 构建任务列表
tasks = [
    # 作用是将协程对象包装成一个任务对象
    asyncio.ensure_future(foo(1)),
    asyncio.ensure_future(foo(2)),
    asyncio.ensure_future(foo(3))
]
loop.run_until_complete(asyncio.wait(tasks))
for i in tasks:
    print(i.done())  # 判断任务是否完成
    print(i.result())  # 获取任务的返回值
    i.add_done_callback(callback)  # 添加回调函数, 回调函数就是任务执行完毕之后的回调函数

