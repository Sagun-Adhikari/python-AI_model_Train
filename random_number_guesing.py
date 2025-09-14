import random
no=random.randint(1,10)
print("welcome to number guessing game")
print("you have 3 chance to guess the number between 1 to 10")  
for i in range(3):
    guess=int(input("enter your guess: "))
    if guess==no:
        print("congratulation you win")
        exit()
    elif guess<no:
        print("your guess is too low")
    else:
        print("your guess is too high")
print("sorry you lose the number is",no)
