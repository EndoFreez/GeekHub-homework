# 2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй
# повинна повертати якийсь результат (напр. інпут від юзера, результат
# математичної операції тощо). Також створiть четверту ф-цiю, яка
# всередині викликає 3 попередні, обробляє їх результат та також
# повертає результат своєї роботи. Таким чином ми будемо викликати одну
# (четверту) функцiю, а вона в своєму тiлi ще 3.

def sq_vs_fact():
	a = int(input("square_num: "))
	def square_num(a):
		if a >= 0:
			return a ** 2

	b = int(input("factorial num: "))
	def fact(b):
		factorial = 1
		for i in range(1, b +1):
			factorial = factorial*i
		return factorial

	a = square_num(a)
	b = fact(b)
	def comparison_of(a, b):
		if a == b:
			return print("Квадрат числа №1 дорівнює факторіалу числа №2!")
		elif a > b:
			return print("Квадрат числа №1 більше факторіалу числа №2!")
		elif a < b:
			return print("Квадрат числа №1 менше факторіалу числа №2")
		else:
			print("oooops")
	return comparison_of(a, b)

sq_vs_fact()

