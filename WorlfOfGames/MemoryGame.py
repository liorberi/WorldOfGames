import time
from random import randrange
import os



def generate_sequence(difficulty):
    list = []
    for num in range(difficulty):
        list.append(randrange(1, 101))
    print(list)
    time.sleep(3)
    cls()
    return list

def get_list_from_user(difficulty):
    list= []
    for num in range(difficulty):
        list.append(int(input("enter number between 1-101 \n")))
    return list

def is_list_equal(randlist, userlist):
    randlist.sort()
    userlist.sort()
    if randlist == userlist:
        return True
    else:
        return False

def play(difficulty):
    randlist = generate_sequence(difficulty)
    userlist = get_list_from_user(difficulty)
    print("the random list is: ")
    print(randlist)
    print("the user list is: ")
    print(userlist)
    if is_list_equal(randlist, userlist):
        print("the user as won the game")
    else:
        print("the user as lost the game")


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
