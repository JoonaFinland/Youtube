import random
n = random.randint(1, 99)
while n != "guess":
    guess = int(input("Enter an integer from 1 to 99: "))
    if guess < n:
        print("guess is low")
    elif guess > n:
        print("guess is high")
    else:
        print("you guessed it!")
        break
    print
