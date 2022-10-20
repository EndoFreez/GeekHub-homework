# 6. Написати функцію, яка буде реалізувати логіку циклічного зсуву
# елементів в списку. Тобто функція приймає два аргументи: список і
# величину зсуву (якщо ця величина додатна - пересуваємо з кінця на
# початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#   Наприклад:
#  fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#  fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]


def landslide(some_list, shift):
	lded = some_list[-shift:] + some_list[:-shift]
	return lded

list1 = [1, 2, 3, 4, 5]
shift = int(input(":"))
print(landslide(list1, shift))

