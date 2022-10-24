# 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від
# 0 до 1000, и яка вертатиме True, якщо це число просте і False - якщо ні.

def is_prime(num):
	if num in range(0, 1000):
		if num <= 1:
			return False
		for i in range(2, num):
			if num % i == 0:
				return False
		return True
			
		
num = int(input("Перевірити число: "))
print(is_prime(num))

