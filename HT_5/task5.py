# 5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить
# всі числа Фібоначчі, що не перевищують його.

def fibonacci(r):
	fib = []
	a = 1
	b = 0
	while a <= r:
		fib += [a]
		a, b = a + b, a 
	return print(*fib)


r = int(input("Границя діапазону: "))		
fibonacci(r)