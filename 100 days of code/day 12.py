# DAY - 12
# SCOPE

enemies = 1

def increase_enemies():
  return enemies + 1

enemies = increase_enemies()

print(enemies)

# --------------------------------------------------------

import random

def game():
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  attempts = int('0')

  if level == 'hard':
    attempts = 5
  else:
    attempts = 10

  number_computer_guessed = random.randint(0, 100)
  print(f"You have {attempts} attempts remaining to guess the number.")

  def compare(computer_number, guessed_number):
    if computer_number>guessed_number:
      return 'Too low.'
    elif computer_number<guessed_number:
      return 'Too high.'
    else:
      return 'Match'

  exit = 'n'

  while exit == 'n':

    Guessed_number = int(input("Make a guess: "))

    if attempts == 1:
      print(compare(number_computer_guessed, Guessed_number))
      if print != 'Match':
        print("You've run out of guesses, you loose.")
        exit = 'y'
      else:
        print(f"You got it! The answer is {number_computer_guessed}")
        exit = 'y'
    else:
      if compare(number_computer_guessed, Guessed_number) != 'Match':
        print(compare(number_computer_guessed, Guessed_number))
        print("Guess again")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
      else:
        print(f"You got it! The answer is {number_computer_guessed}")
        exit = 'y'

game()

# _____________________ END ____________________________________