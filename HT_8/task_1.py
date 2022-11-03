# 1. Програма-світлофор.
# Створити програму-емулятор світлофора для авто і пішоходів. Після
# запуска програми на екран виводиться в лівій половині - колір
# автомобільного, а в правій - пішохідного світлофора. Кожну 1 
# секунду виводиться поточні кольори. Через декілька ітерацій - 
# відбувається зміна кольорів - логіка така сама як і в звичайних
# світлофорах (пішоходам зелений тільки коли автомобілям червоний).
# Приблизний результат роботи наступний:
#      Red        Green
#      Red        Green
#      Red        Green
#      Red        Green
#      Yellow     Red
#      Yellow     Red
#      Green      Red
#      Green      Red
#      Green      Red
#      Green      Red
#      Yellow     Red
#      Yellow     Red
#      Red        Green

from time import sleep

ligths = ["Red", "Green", "Yellow"]
while True:
      for _ in range(4):
         print(f'{ligths[0]}        {ligths[1]}')
         sleep(1)
      for _ in range(2):
         print(f'{ligths[2]}     {ligths[1]}')
         sleep(1)
      for _ in range(4):
         print(f'{ligths[1]}      {ligths[0]}')
         sleep(1)
      for _ in range(2):
         print(f'{ligths[2]}     {ligths[0]}')
         sleep(1)
