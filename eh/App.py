from Class import PinError, BalanceError, WithdrawAmountError
from Function import atm

try:
    atm()
except PinError as pe:
    print(f'PinError: {pe}')
except WithdrawAmountError as wae:
    print(f'WithdrawAmountError: {wae}')
except BalanceError as be:
    print(f'BalanceError: {be}')