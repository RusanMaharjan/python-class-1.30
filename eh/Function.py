from Class import BalanceError, WithdrawAmountError, PinError

def atm():
    pin = 1234
    balance = 50000
    
    user_pin = int(input('Enter your pin number: '))
    
    if user_pin == pin: # 123 == 1234 -> False
        amount = int(input('Enter your withdraw balance: '))
    
        if amount < balance: # 5500 < 50000
            if amount % 1000 == 0: # 5500 % 1000 == 0
                print(f'Rs.{amount} has been withdrawn.')
            else:
                raise BalanceError('Withdraw amount must be multiple of 1000.')
        else:
            raise WithdrawAmountError('Withdraw amount must be less than available balance.')
    else:
        raise PinError('Incorrect pin number.')