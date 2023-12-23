def foo():
    print("foo start")
    yield
    print("foo end")
    yield


def bar():
    print("bar start")
    yield
    print("bar end")
    yield


gen_foo = foo()
bar_foo = bar()

next(gen_foo)
next(bar_foo)
next(gen_foo)
next(bar_foo)
