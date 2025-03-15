## Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if self.balance + amount < 0:
            print("Dépot impossible, le compt serait inférieur à 0")

        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Retrait impossible")
            return None

        self.balance -= amount

    def display_balance(self):
        print(f"{self.account_holder} à {self.balance}€")


bankAccount = BankAccount("arthur", 25000)
bankAccount.display_balance()
bankAccount.deposit(10000)
bankAccount.display_balance()
bankAccount.withdraw(50000)
bankAccount.withdraw(25000)
bankAccount.display_balance()
