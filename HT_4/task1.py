# 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця 
# вiд 1 до 12) та яка буде повертати пору року, до якої цей мiсяць 
# належить (зима, весна, лiто або осiнь). У випадку некоректного 
# введеного значення - виводити відповідне повідомлення.

def get_season(month_num):
	winter = [1, 2, 12]
	spring = [3, 4, 5]
	summer = [6, 7, 8]
	autumn = [9, 10, 11]
	if month_num in winter:
		print("Зима")
	elif month_num in spring:
		print("Весна")
	elif month_num in summer:
		print("Літо")
	elif month_num in autumn:
		print("Осінь")
	else:
		print("Такого місяця не існує!")
	return month_num

month_num = int(input("Введіть номер місяця: "))
get_season(month_num)