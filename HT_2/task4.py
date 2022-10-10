# Write a script which accepts a <number> from user and then <number>
# times asks user for string input. At the end script must print out 
# result of concatenating all <number> strings.

result = ""
num_times = int(input("Times: "))
for i in range(num_times):
	result += input("Text: ")
print(result)
