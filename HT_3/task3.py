# Write a script to remove empty elements from a list.

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
dict_4 = {}
for i in (dict_1, dict_2, dict_3):
	dict_4.update(i)
print(dict_4)

# цей варіант підказали)

dict_5 = (dict_1 | dict_2 | dict_3)
print(dict_5)
