# 3. Програма-банкомат.


import csv
import json


def start():

    def login(user, password):

        try:
            with open("users.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["User"] == user and row["Password"] == password:
                        return True
                return False
        except FileNotFoundError:
            print("Something wrong!@#$%")


    def check_balance(user):

        with open(user + "_balance.txt", 'r') as balance:
            return balance.read()


    def replenish(user):

        try:
            deposit = int(input("Deposit amount: "))
            with open(user + "_balance.txt", "r+") as file:
                lines = file.readlines()

                if deposit > 0:
                    new_bal = int(lines[0]) + deposit
                    print(f'Your new balance is {new_bal}.')
                    file.seek(0)
                    file.write(str(new_bal))
                    return new_bal
                else:
                    print("You can't do this!")

        except FileNotFoundError:
            print("You have no balance at our bank!") 
        except ValueError:
            print("Incorrect amount")


    def withdraw(user):

        try:
            money = int(input("Enter the amount: "))
            balance = int(check_balance(user))
            if money <= 0:
                print("You can't do this")
                return print(balance)
            if money > balance:
                print("You don't have enough funds")
                return f"Try again, you have {balance}"
            with open(user + "_balance.txt", 'r+') as file:
                file.write(str(balance - money))
            transaction = {"withdrawn funds" : money}
            with open(user + "_transactions.json", "a") as t_file:
                json.dump(transaction,t_file)
            return print(f"You did it, now you have {check_balance(user)}")

        except ValueError:
            print("Incorrect amount")


        
    user = input("Username: ")
    password = input("Password: ")

    if login(user, password) == False:
        print("Incorrect login or password, try again.")
        return start()
    else:
        try:
            print("______________________________________")
            print("| To check your balance     press  1 |")
            print("| To replenish your balance press  2 |")
            print("| To withdraw money         press  3 |")
            print("| To change user            press  4 |")
            print("|____________________________________|")
            option = int(input("Choose your option: "))
            if option == 1:
                print(f'Your balance is {check_balance(user)}')
                return start()
            if option == 2:
                return replenish(user)
            if option == 3:
                return withdraw(user)
            if option == 4:
                return start()
        except ValueError:
            print("Enter correct option")

if __name__ == "__main__":
    start()