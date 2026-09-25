from ErrorHandling import DepositAmountError, WithdrawAmountError

import random
class Bank:
    def __init__(self, name, job, initial_balance):
        self.name = name
        self.job = job
        self.initial_balance = initial_balance
        self.account_number = self.name[1:3]+"".join(str(random.randint(1, 9)) for i in range(16))+'NB'

    # deposit amount
    def depositAmount(self, amount):
        if amount >= 100:
            self.initial_balance += amount
            print(f'Rs.{amount} has been deposited in A/C no. {self.account_number}.')
        else:
            raise DepositAmountError('Deposit amount must be more than Rs.100.')

    # withdraw amount
    def withdrawAmount(self, amount):
        if amount < self.initial_balance:
            self.initial_balance -= amount
            print(f'Rs.{amount} has been withdrawn from A/C no. {self.account_number}.')
        else:
            raise WithdrawAmountError('Insufficient balance.')

    # show details
    def show_details(self):
        print(f'Account Holder Name: {self.name}')
        print(f'Account Holder Job: {self.job}')
        print(f'Initial Balance: Rs.{self.initial_balance}')
        print(f'Account Number: {self.account_number}')