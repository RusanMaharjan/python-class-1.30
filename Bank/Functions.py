from Storage import all_accounts
from ErrorHandling import AccountNumberError, DepositAmountError
from Bank import Bank

# find account
def findAccountByAccountNumber(acc_number):
    for account in all_accounts:
        if account.account_number == acc_number:
            return account
    else:
        raise AccountNumberError('No account found with given account number.')

# create account
def createAccount():
    name = input('Enter your name: ')
    job = input('Enter your job title: ')
    initial_balance = int(input('Enter your initial balance: '))

    if initial_balance > 100:
        b = Bank(name, job, initial_balance)
        all_accounts.append(b)
        print(f'Account created with name {name} and A/C no. {b.account_number}.\nRs.{initial_balance} has been deposited.')
    else:
        raise DepositAmountError('Initial deposit amount must be more than Rs.100.')