# While loop practice 27th November

import random

secret_number = random.randint(0, 10)

#print(secret_number)

guess_count=0
guess_limit = 5

while guess_count < guess_limit:
   guess = int(input("Guess: "))
   guess_count += 1
   if guess == secret_number:
       print("You won ")
       print("The secret number was ",secret_number)
       break
else:
    print("Sorry you failed")



