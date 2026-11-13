import random

number = random.randint(1, 100)

print("Guess the number between 1 and 100")
print("You have 10 chances.")

for i in range(10):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("You Win!")
        break

    elif guess < number:
        print("Try a bigger number.")

    else:
        print("Try a smaller number.")

else:
    print("You Lose!")
    print("The correct number was:", number)