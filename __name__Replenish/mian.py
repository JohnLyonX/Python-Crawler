# 补充__name__的作用
import model01
import model02

if __name__ == '__main__':
    model01.model01()
    model02.model02()
    print('我是程序: ' + __name__)
