# 1. Write a script that will run through a list of tuples and replace
# the last value for each tuple. The list of tuples can be hardcoded. 
# The "replacement" value is entered by user. The number of elements in
# the tuples must be different.

tuples_list = [
	("1", 2, True, "kaka", ),
	("tuple", 13, 'list', 4, "2333", "kik", ),
	(1, 2, 3, "16", False, ), ()
]
change_for = input("Replace: ")
print([x[:-1] + (change_for,) if len(x) != 0 else () for x in tuples_list])
