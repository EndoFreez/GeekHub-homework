# 6. Напишіть функцію,яка приймає рядок з декількох слів і повертає
# довжину найкоротшого слова. Реалізуйте обчислення за допомогою
# генератора в один рядок.

def shortest_in(some_string):
    return min([len(word) for word in some_string.split()])


print(f'Довжина найкоротшого слова: {shortest_in("What are you doing here?")}.')
