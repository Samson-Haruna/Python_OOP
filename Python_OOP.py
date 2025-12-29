# Bank mangement system

class BankAccount:
    def __init__(self,account_name,account_number,balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"you have deposited ₦{amount} and your balance is ₦{self.balance}")

        else:
            print("Amount is to small to be deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"you have been debited ₦{amount} and your balance is ₦{self.balance}")

        else:
            print("insuficient balance to make this withdrawal")

   
    def checkbalance(self):

        a = (input('enter account name: '))
        b = (int(input('enter account number: ')))
        
        if a != self.account_name and b != self.account_number:
            print('account name and/or account is incorrect...please try again')

        else:
            print(f"your account balance is ₦{self.balance}")

"""
The SavingsAccount class is used to show the concept of INHERITANCE
the SavingsAccount class is inheriting some of the attributes in the BankAccount class
SavingdAccount = child class
BankAccount = parent class
"""
class SavingsAccount(BankAccount):
    def __init__(self,account_name,account_number,balance, interest_rate=0.05):
        super().__init__(account_name,account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ₦{interest}. New balance: ₦{self.balance}")




account1 = BankAccount("Samson", 5005,0)

#account1.deposit(10000)
#account1.deposit(50000)
#account1.withdraw(20000)
#account1.checkbalance()
account2 = SavingsAccount("john",1001,0)
account2.deposit(30000)
account2.deposit(5000)
account2.apply_interest()
#account2.apply_interest()



