# 3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію
# цієї функції. Тобто щоб її можна було використати у вигляді:
# for i in my_range(1, 10, 2):
#       print(i)
#   1
#   3
#   5
#   7
#   9
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати
# документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
# P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5)
# тощо). Подивіться як веде себе стандартний range в таких випадках.


def my_range(start, stop = None, step = 1):
    if step == 0:
        raise ValueError
    if stop == None:
        stop = start
        start = 0
    if step > 0:
        if start > stop:
            raise ValueError
        else:
            while start < stop:
                yield start
                start += step
    if step < 0:
        if start < stop:
            raise ValueError
        else:
            while start > stop:
                yield start
                start += step

for t in my_range(5):
    print(t)

for p in my_range(1, 10, 2):
    print(p)

for i in my_range(-10, -20, -1):
    print(i)

for b in my_range(-10, 20, -5):
    print(b)
