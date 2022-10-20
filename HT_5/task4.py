# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок
# і кінець діапазона, і вертатиме список простих чисел всередині цього
# діапазона. Не забудьте про перевірку на валідність введених даних та
# у випадку невідповідності - виведіть повідомлення.

def prime_list(start, end):
	list1 = []
	for num in range(start, end):
		is_prime = True
		if num < 1:
			return "Просте число має бути >1"
		for i in range(2, num):
			if num % i == 0:
				is_prime = False
		if is_prime and num >= 2:
			list1.append(num)
	return list1
		

start = int(input("Початок діапазону: "))
end = int(input("Кінець діапазону: "))
print(prime_list(start, end))