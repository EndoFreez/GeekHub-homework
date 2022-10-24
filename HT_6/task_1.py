# 1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти
# користувачів (ім'я та пароль). Функція повинна приймати три аргументи:
# два - обов'язкових (<username> та <password>) і третій - необов'язковий
# параметр <silent> (значення за замовчуванням - <False>).
#Логіка наступна:
#    якщо введено правильну пару ім'я/пароль - вертається True;
#    якщо введено неправильну пару ім'я/пароль:
#        якщо silent == True - функція повертає False
#        якщо silent == False - породжується виключення LoginException
# (його також треба створити =))

class LoginException(Exception):
	pass

def lpvalidator(username, password, silent = False):

	data = [("pavel", "grenkilublu"), ("kolyamba", "anarhist777"),
	("Geekhub", "karrrammmbaaa"), ("kotolub", "kiskismyamya3000"),
	("kolombo", "shishkorvach")]
	if (username, password) in data:
		return True
	else:
		if silent == True:
			return False
		elif silent == False:
			return LoginException("Something wrong!!!")

print(lpvalidator("kolyamba", "anarhist777", False))
print(lpvalidator("kolombo", "shishkorvach", True))
print(lpvalidator("pavel", "grenkilublu", True))
print(lpvalidator("kotolub", "shishkorvach", True))
print(lpvalidator("petia", "buhanka"))


