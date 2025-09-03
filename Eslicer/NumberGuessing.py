import random

def number_guessing():
  print("I'm thinking of a number between 1 to 100 ... ")

  secret_number = random.randint(1, 100)
  attempts = 0

  while True:
    try:
      guess = int(input("Take a guess: "))
      attempts += 1

      if guess < secret_number:
        print("too low! Try again.")
      elif guess > secret_number:
        print("too high! Try again.")
      else:
        print(f"Congratulations! You guessed it right in {attempts} attempts.")
        break

    except ValueError:
      print("please enter valid number")



if __name__ == '__main__':
  number_guessing()