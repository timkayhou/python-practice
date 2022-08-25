# Guess number game
import random
countTimes = 3
number = random.randint(1, 10)
while countTimes > 0:
    temp = input("Guess the number from 0 to 9: ")
    while not temp.isdecimal():
        print("Please input int.")
        temp = input("Guess the number from 1 to 10: ")
    guess = int(temp)
    if guess == number:
        print("You win!")
        break
    elif guess < number:
        print(">", guess)
    else:
        print("<", guess)
    countTimes -= 1
else:
    print("You lost.")
print("It's", number)
