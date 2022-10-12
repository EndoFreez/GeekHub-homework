# 5. Write a script to remove values duplicates from dictionary.

dict1 = {'A': 3, 'B': 17, 'C': 22, 'D': 3, 'E': 22, 'F': 17}
a = {i: key for key, i in dict1.items()}
b = {i: key for key, i in a.items()}
print(b)
