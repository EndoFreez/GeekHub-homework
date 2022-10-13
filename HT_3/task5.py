# 5. Write a script to remove values duplicates from dictionary.

dict1 = {'A': 3, 'B': 17, 'C': 22, 'D': 3, 'E': 22, 'F': 17}
dict2 = {}
for key,value in dict1.items():
    if value not in dict2.values():
        dict2[key] = value
print(dict2)
