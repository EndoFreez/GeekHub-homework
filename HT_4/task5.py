# 5. Ну і традиційно - калькулятор Повинна бути 1 
# функцiя, яка приймає 3 аргументи - один з яких операцiя, яку зробити!
# Аргументи брати від юзера (можна по одному - окремо 2, окремо +,
# окремо 2; можна всі разом - типу 2 + 2). Операції що мають бути
# присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними 
# значеннями на предмет помилок!

def calc(a, b, c):
	try:
		if b == "+":
			return print(a + c)
		if b == "-":
			return print(a - c)
		if b == "*":
			return print(a * c)
		if b == "/":
			return print(a / c)
		if b == "%":
			return print(a % c)
		if b == "//":
			return print(a // c)
		if b == "**":
			return print(a ** c)
	except ZeroDivisionError:
		return print("з 0 не спрацює")
	else:
		return print("Не підримуєма операція!")

a = int(input("Перша цифра: "))
b = input("+, -, *, /, %, //, **,:")
c = int(input("Друга цифра: "))
calc(a, b, c)
