class LoginException(Exception):
    pass


def login_pass(username, password):

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

    if 3 >= len(username) < 50:
        raise LoginException(">3<50")
    if len(password) < 8:
        raise LoginException("Має бути 8 або більше символів у паролі!")
    if not check_num(password) or not check_capital(password):
        raise LoginException("Має бути не менше 1 великої літери та цифри")
    else:
        return print("Хух, ви це зробили, вітаю!!!")

login_pass("Kovbasar1", "Kosalsjd123")
login_pass("Ko", "sobaka123")
