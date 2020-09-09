
name = input("Welcome, please enter your name: ")

print("Hello   " + name + "! welcome to the World of Games (WoG). Here you can find many cool games to play") 

load_game = 0
while int(load_game) < 1 or int(load_game) > 3:
   load_game = int(input("Please choose a game to play:\n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n   2. Guess Game - guess a number and see if you chose like the computer\n   3. Currency Roulette - try and guess the value of a random amount of USD in ILS  "))   
   

level_difficult = int(input("Please choose game difficulty from 1 to 5:   "))
level_difficult = 0
while int(level_difficult) < 1 or int(level_difficult) > 5:
   level_difficult = int(input("Please choose game difficulty from 1 to 5:   "))
