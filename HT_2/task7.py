# Write a script to concatenate all elements in a list into a string
# and print it. List must include both strings and integers and must
# be hardcoded.

hardcoded_list = ["a", "True", 300, 200, 100, "v", 1, "?"]
string =' '.join(map(str, hardcoded_list))
print(string)
