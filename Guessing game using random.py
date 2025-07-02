import random
secret_Number=random.randint(0,100)
no_of_guesses = 0
while True:
    Guess = int(input("Please guess a number between 0 and 100:   "))
    if secret_Number>Guess:
        no_of_guesses+=1
        print(f"Your guess {Guess} is lower than the secret number\n Number of Guesses made= {no_of_guesses}\n")
        continue
    elif secret_Number<Guess:
        no_of_guesses += 1
        print(f"Your guess {Guess} is higher than the secret number\n Number of Guesses made= {no_of_guesses}\n")
        continue
    else:
        no_of_guesses +=1
        print(f"Congratulations you made the right guess\n\nIt took you {no_of_guesses} guesses\n")
        break