import random

# GETTING A RANDOM NUMBER 1-10
def get_number():
    return random.randint(1, 10)

# CHECKING THE GUESS
def check_guess(guess_num, rand):
    if guess > rand:
        print("Too high...")
    if guess < rand:
        print("Too low...")
    if guess == rand:
        return True

# INTRO AND CHOOSING DIFFICULTY - LIVES
print("Welcome to the guessing game. Try to guess the correct number" + '\n')

difficulty = input("Choose a difficulty: 'E' for easy, 'M' for medium or 'H' for hard. " + '\n')
random_number = get_number()

if difficulty == 'E':
    lives = 10
elif difficulty == 'M':
    lives = 5
elif difficulty == 'H':
    lives = 1
else:
    difficulty = input("Enter proper character: " + '\n')

print("You have: {} lives left. Start guessing! ".format(lives) + '\n')


# LOOP IF GUESS = WRONG
guess = 0
count = 0

while guess != random_number:
  guess = int(input())
  lives = lives - 1
  count = count + 1

  if check_guess(guess, random_number):
      print("You won the game! You guessed {} times".format(count))
      break

  elif lives == 0:
      print("You lost the game. You guessed {} times".format(count))
      print("The number was {} ".format(random_number))
      break
