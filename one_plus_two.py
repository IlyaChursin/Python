import math
import time
import functools


def timefunc(func):
    @functools.wraps(func)
    def need_time(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Функция: {func.__name__}, Затраченное время: {time_elapsed}\n")
        return res

    return need_time

@timefunc
def square(width,length):
    SQFT_PER_ACRE = 43560
    result = (width * length) / SQFT_PER_ACRE
    print("Площадь в акрах ->", result)

@timefunc
def speed(hight):
    acceleration = 9.8
    result = math.sqrt(2*acceleration*hight)
    print("Скорость при касании земли ->", round(result))


hight = float(input("Введите высоту в метрах\n"))
speed(hight)

width = float(input("Введите ширину участка в футах\n"))
length = float(input("Введите длину участка в футах\n"))
square(width,length)