import random
from app import logo
easy  = 10
hard = 5

def difficulty():
      level = input("enter 'easy' or 'hard'")
      if level == "easy":
          return easy
      else:
          return hard
def guess(answer,guess_value,turn):
    if guess_value == answer:
        print("You guessed right")
        print("conguratulation !")
        print(logo)
        return turn
    elif guess_value > answer:
        print("You guessed higher")
        return turn -1
    elif guess_value < answer:
        print("You guessed lower")
        return turn -1


def game():
    answer = random.randint(1, 100)
    
    print(answer)
    print("guess the number between 1 and 100")
    turns = difficulty()
    guess_value = 0
    while guess_value != answer:
        guess_value = int(input("Guess the number: "))

        turns = guess(answer, guess_value,turns)
        if turns == 0:
            print("game over")
            return
        elif guess_value != answer:
            print(f"you have {turns} left")
            print("guess again")


game()



