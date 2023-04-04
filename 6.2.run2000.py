
import timeit


def timer(func, *args, **kwargs):
    elapsed_time = timeit.timeit(lambda: func(*args, **kwargs), number=1)
    return elapsed_time


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")












