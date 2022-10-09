# Write a script which accepts a <number> from user and print out a sum
# of the first <number> positive integers.

sum_of_first_positive = int(input("Number: "))
if sum_of_first_positive >= 1:
	print(sum_of_first_positive * (sum_of_first_positive + 1) / 2)
else:
	print(None)