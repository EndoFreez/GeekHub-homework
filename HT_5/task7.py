# 7. Написати функцію, яка приймає на вхід список (через кому),
# підраховує кількість однакових елементів у ньому і виводить 
# результат. Елементами списку можуть бути дані будь-яких типів.
# Наприклад: 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3,
# foo -> 2, [1, 2] -> 2, True -> 1"

from collections import Counter


list1 = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]


def count_el(list1):
	str1 = Counter(map(str, list1))

	return str1


print(count_el(list1))