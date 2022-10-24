# 2. Створіть функцію для валідації пари ім'я/пароль за наступними 
# правилами:
#  - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#  - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#  цифру;
#  - якесь власне додаткове правило :)
#  Якщо якийсь із параметрів не відповідає вимогам - породити виключення
# із відповідним текстом.

class LoginException(Exception):
    pass

def check_num(password):
    for i in password:
        if i.isdigit():
            return True
    return False

def check_capital(password):
    for i in password:
        if i.isupper():
            return True
    return False

def login_pass(username, password):
    if 3 > len(username) < 50:
        raise LoginException(">3<50")
    if len(password) < 8:
        raise LoginException("Має бути 8 або більше символів у паролі!")
    if not check_num(password) or not check_capital(password):
        raise LoginException("Має бути не менше 1 великої літери та цифри")
    else:
        return print("Хух, ви це зробили, вітаю!!!")

login_pass("Kovbasar1", "sdoskkjjd1")