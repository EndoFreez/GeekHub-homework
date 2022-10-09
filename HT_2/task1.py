# 1. Write a script which accepts a sequence of comma-separated numbers
# from user and generates a list and a tuple with those numbers.

sepnum = input("Comma-separated: ")
lis = sepnum.split(",")
print(lis)
print(tuple(lis))