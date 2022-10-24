# 3. На основі попередньої функції (скопіюйте кусок коду) створити
# наступний скрипт:
#   а) створити список із парами ім'я/пароль різноманітних видів 
# (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись
# валідатором, перевірить ці дані і надрукує для кожної пари значень
# відповідне повідомлення, наприклад:
#      Name: vasya
#      Password: wasd
#      Status: password must have at least one digit
#      -----
#      Name: vasya
#      Password: vasyapupkin2000
#      Status: OK
#   P.S. Не забудьте використати блок try/except ;)

class LoginException(Exception):
    pass

def login_pass(username, password):

    if 3 >= len(username) < 50:
        raise LoginException(">3<50")
    if len(password) < 8:
        raise LoginException("Має бути 8 або більше символів у паролі!")
    if not any(i.isdigit() for i in password):
        raise LoginException("Пароль має містити цифри")
    if not any(i.isupper() for i in password):
        raise LoginException("Пароль має містити великі літери")
    else:
        return print("Хух, ви це зробили, вітаю!!!")

data = [("Pavelito", "Grenkilublu111"), ("kolyamba", "anarhist777"),
    ("Geekhub", "karrrammmbaaa"), ("kot", "kiskismyamya3000"),
    ("kolombo", "shishkorvach")]

for i in data:
    try:
        print("Username:", i[0])
        print("Password:", i[1])
        login_pass(i[0], i[1])
    except LoginException as error:
        print(f"Something wrong: {error}")
    print("-----------")

