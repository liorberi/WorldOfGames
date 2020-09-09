from currency_converter import CurrencyConverter
from random import randrange



def get_money_interval(difficulty,value):
    c = CurrencyConverter()
    currencyILS = c.convert(1, 'USD', 'ILS')
    t = value * currencyILS
    interval = [t - (5 - difficulty), t + (5 - difficulty)]
    return interval


def get_guess_from_user(value):
    userGuess = float(input("enter the value of " + str(value) + " USD in ILS\n"))
    return userGuess


def play(difficulty):
    value = randrange(1, 100)
    print("The value is: " + str(value))
    intval = get_money_interval(difficulty, value)
    usrGuess = get_guess_from_user(value)
    if intval[0] <= usrGuess <= intval[1]:
        print("the user have won the game")
        return True
    else:
        print("the user as lost the game")
        return False
