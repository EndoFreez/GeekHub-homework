# Write a script which accepts a <number> from user and then <number>
# times asks user for string input. At the end script must print out 
# result of concatenating all <number> strings.

num_times = int(input("Times: "))
for con_g in range(num_times):
	some_string = num_times*(input("Text: "))
print(some_string)