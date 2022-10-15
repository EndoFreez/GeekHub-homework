# 4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe kdno400
# we(nw,kowe%00koi!jn35pijnp4 6ijk5j78p3kj546p4 65jnpoj35po6j345" -> 
# просто потицяв по клавi =)
# Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього та
# яка обробляє наступні випадки:
# -  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину
# рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок
# без цифр та знаків лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

a = "f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345"
b = "f98neroi4nr0c3n30irn03iereen3jgf304"
c = "f98nero#i4nr0c3))n30i0"
def format_string(some_crazy_string):
	if len(some_crazy_string) > 50:
		only_num = ""
		for i in some_crazy_string:
			if i.isdigit():
				only_num += i
		print("Лише цифри з рядку:", only_num)
	elif len(some_crazy_string) >= 30 and len(some_crazy_string) <= 50:
		print("Довжина рядка:", len(some_crazy_string))
	elif len(some_crazy_string) < 30:
		sum_of_num = 0
		letter_str = ""
		for i in some_crazy_string:
			if i.isdigit():
				sum_of_num += int(i)
			if i.isalpha():
				letter_str += i
		print("Сума цифер у рядку:", sum_of_num)
		print("Лише літери:", letter_str)
format_string(a)
format_string(b)
format_string(c)
