# 案例：数据生成器
def get_data():
    for i in range(1, 100000):
        yield i


gen = get_data()

for i in gen:
    print(i)
