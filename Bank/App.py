from Functions import createAccount, findAccountByAccountNumber
from ErrorHandling import AccountNumberError, DepositAmountError, WithdrawAmountError

def bankApp():
    while True:
        print('1. Create Account')
        print('2. Deposit Amount')
        print('3. Withdraw Amount')
        print('4. User Details')
        print('5. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            # ask user do they really want to create account?
            y_n = input('Do you want to create account? ')

            if y_n == 'y':
                print('Create Account')
                print('-'*45)
                try:
                    createAccount()
                except DepositAmountError as de:
                    print(f'Error: {de}')
            else:
                print('Continue with your transaction.')
            
        elif choice == 2:
            y_n = input('Do you want to deposit amount? ')
            if y_n == 'y':
                print('Deposit Amount')
                print('-'*45)
                try:
                    acc_number = input('Enter your account number: ')
                    find_acc = findAccountByAccountNumber(acc_number) # fetch account number and store users object

                    if find_acc:
                        amount = int(input('Enter your deposit amount: '))
                        find_acc.depositAmount(amount)
                except AccountNumberError as ae:
                    print(f'Error: {ae}')
                except DepositAmountError as de:
                    print(f'Error: {de}')
            else:
                print('Continue with your transaction.')

        elif choice == 3:
            y_n = input('Do you want to withdraw amount? ')
            if y_n == 'y':
                print('Withdraw Amount')
                print('-'*45)
                try:
                    acc_number = input('Enter your account number: ')
                    find_acc = findAccountByAccountNumber(acc_number)
        
                    if find_acc:
                        amount = int(input('Enter your withdraw amount: '))
                        find_acc.withdrawAmount(amount)
                except AccountNumberError as ae:
                    print(f'Error: {ae}')
                except WithdrawAmountError as we:
                    print(f'Error: {we}')
            else:
                print('Continue with your transaction.')
                
        elif choice == 4:
            y_n = input('Do you want to display user details? ')
            if y_n == 'y':
                print('User Details')
                print('-'*45)
                try:
                    acc_number = input('Enter your account number: ')
                    find_acc = findAccountByAccountNumber(acc_number)

                    if find_acc:
                        find_acc.show_details()
                except AccountNumberError as ae:
                    print(f'Error: {ae}')
            else:
                print('Continue with your transaction.')
        elif choice == 5:
            print('Thank you for choosing us.')
            break
        else:
            print('Invalid Choice.')