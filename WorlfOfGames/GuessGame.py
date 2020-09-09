from random import randrange

# generate a random number between 1 to difficulty
def generate_number(difficulty):
    return (randrange(1, difficulty))


# get a number from user between 1 to difficulty
def get_guess_from_user(difficulty):
    return int(input("enter number between 1 to " + str(difficulty) + "\n"))


# compare between secret number to user number
def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False

# main method calling previous methods.
def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    print("secret number is: " + str(secret_number))
    print("user number is: " + str(user_guess))
    if compare_results(secret_number, user_guess):
        print("the user as won the game")
    else:
        print("the user as lost the game")

