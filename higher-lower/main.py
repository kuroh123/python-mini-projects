from art import logo, vs
from game_data import data
import random

print(logo)
def choose_b(a):
    possible_b = data[random.randint(0, len(data) - 1)]
    if a == possible_b['name']:
        choose_b(a)
    else:
        return possible_b

game_end=False
score=0
a = data[random.randint(0, len(data) - 1)]
b = choose_b(a['name'])

while not game_end:
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    if (user_input.lower() == 'a' and a['follower_count'] > b['follower_count']) or (user_input.lower() == 'b' and b['follower_count'] > a['follower_count']):
        score += 1
        a = b
        b = choose_b(a['name'])
        print(f"You're right! Score: {score}")
        print("******************************")
    else:
        game_end = True
        print(f"Sorry, that's wrong. Final score: {score}")