import random

# this was my guess at the challenge
number_in_my_head = random.randint(1, 100)
guess = eval(input("Guess the value of the number in my head: "))

for i in range(5):
  if number_in_my_head == guess:
    print("YOU WON THE GAME!!!")
  elif number_in_my_head > guess:
    print("The number was higher...womp womp")
    guess = eval(input("Guess the value of the number in my head: "))
  elif number_in_my_head < guess:
    print("The number was lower...womp womp")
    guess = eval(input("Guess the value of the number in my head: "))

# CHALLENGE:
#
# Ask the user to guess the value of number_in_my_head.
#
# If the guess matches the number_in_my_head,
# tell the user that they won the game.
#
# Otherwise, display a message telling them whether
# the number was higher or lower.
#
# Bonus: If they don't guess the number, let them guess again.


