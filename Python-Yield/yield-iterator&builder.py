# yield: 迭代器和生成器: 优化存储

def get_data():
    print("start")
    yield 1  # 暂时返回保存对象
    print("come back")
    yield 2
    print("come back2")
    yield 3
    print("end")


gen = get_data()
print(gen)

ret = next(gen)
print(ret)
ret = next(gen)
print(ret)
