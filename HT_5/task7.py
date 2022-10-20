# 7. Написати функцію, яка приймає на вхід список (через кому),
# підраховує кількість однакових елементів у ньому і виводить 
# результат. Елементами списку можуть бути дані будь-яких типів.
# Наприклад: 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3,
# foo -> 2, [1, 2] -> 2, True -> 1"

from collections import Counter


list1 = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]


def count_el(test_list) -> str:
	str1 = list(map(str,list1))
	count = dict(Counter(str1))
	res = ', '
	print(res.join(f"{a} -> {b}" for a, b in count.items()))

count_el(list1)