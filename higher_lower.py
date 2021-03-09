from game_data import data
from art import logo,vs
from replit import clear
import random

print(logo)

def round(first_choice, second_choice):
  print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
  print(vs)
  print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")

game_over = False
score = 0
choice = random.sample(data, 2)
first_choice = choice[0]
second_choice = choice[1]
while game_over is False:
  round(first_choice, second_choice)
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  followers_1 = first_choice['follower_count']
  print(followers_1)
  followers_2 = second_choice['follower_count']
  print(followers_2)
  if user_choice == 'a' and followers_1 > followers_2:
    score += 1
    first_choice = second_choice
    choice = random.sample(data, 1)
    second_choice = choice[0]
    clear()
    print(logo)
    print(f"Your score is {score}")
  elif user_choice == 'b' and followers_2 > followers_1:
    score += 1
    first_choice = second_choice
    choice = random.sample(data, 1)
    second_choice = choice[0]
    clear()
    print(logo)
    print(f"Your score is {score}")
  else:
    clear()
    print(logo)
    print(f"Wrong answer, your final score is {score}. Game over!!!")
    game_over = True
