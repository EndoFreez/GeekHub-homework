# Write a script which accepts two sequences of comma-separated colors 
# from user. Then print out a set containing all the colors from
# color_list_1 which are not present in color_list_2.

color_list_1 = set(input("set comma-separated list1: ").split(','))
print(color_list_1)
color_list_2 = set(input("set comma-separated list2: ").split(','))
print(color_list_2)
print(color_list_1 - color_list_2)