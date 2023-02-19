# Higher or Lower Game
import random
import os
from art import logo, vs

# Create a dictionary of companies and number of users
questions_dict = {
    "YouTube": 2000000000,
    "Twitter": 329000000,
    "TikTok": 1000000000,
    "FaceBook": 2500000000,
    "Instagram": 1000000000,
    "Snapchat": 347000000,
    "Pinterest": 478000000,
    "Spotify": 406000000,
    "Bing Search": 126000000,
    "Patreon": 6000000,
    "eBay": 135000000,
    "Paypal": 426000000,
    "ChatGPT": 200000000,
    "Google": 4600000000,
    "PornHub": 3300000000,
    "LinkedIn": 830000000,
    "Whatsapp": 2240000000,
    "Reddit": 430000000,
    "Discord": 140000000,
    "Twitch": 140000000,
    "WeChat": 1250000000,
    "Amazon": 300000000,
    "Netflix": 214000000,
}

# make a list of the dictionary keys which allows us the use the keys in our program
keys_list = list(questions_dict)


# Create a function for comparing users choice against both possible choices
# and return True if users choice is the highest choice else return false
def compare(choice_a, choice_b, user_guess):
    largest_number = max(questions_dict[choice_a], questions_dict[choice_b])
    if questions_dict[user_guess] == largest_number:
        return True
    else:
        return False


def main_game():  # Main game function
    # select initial choices for the user by plucking two random keys from the list of keys
    # we use random.sample to prevent duplicate choices
    first_choice, second_choice = random.sample(keys_list, 2)
    game_on = True
    score = 0
    while game_on:  # Main loop for game
        print(logo)
        print(f"Your Current Score: {score}")
        print(f"Compare A: {first_choice}")
        print(vs)
        print(f"\nAgainst B: {second_choice}")

        # User to make a choice
        user_guess = input("\nWhich has more users?: ")
        if user_guess == "a":
            user_guess = first_choice
            # turns users string answer into relevant dict key
            # because we can't check a or b, we need to tie a or b to the proper key
        elif user_guess == "b":
            user_guess = second_choice

        # Calls the compare function and checks if it returned True (Guess was higher)
        # or False if it was the lower value of the choices
        os.system("cls")
        if compare(first_choice, second_choice, user_guess):
            print(f"You got it! {user_guess} has {questions_dict[user_guess]} users!")
            score += 1

        elif not compare(first_choice, second_choice, user_guess):
            print(f"Nope! Sorry.")
            print(f"Final score: {score}")
            game_on = False  # Game ends if compare function returns false

        # This line removes the first choice from the list of choices so that we
        # don't reuse it. Then we make the First Choice (A) equal to the previous second choice (B)
        # so A now becomes B and B is now a new random choice from the keys_list
        if game_on:
            keys_list.remove(first_choice)
            first_choice = second_choice
            second_choice = random.choice(keys_list)

        if len(keys_list) <= 1:
            game_on = False  # Ends the game if the keys_list is empty
            print("You maxed out all the options! Well Done!")
            print(f"Final score {score}")

        if not game_on:
            if input("Do you want to play again? 'y' or 'n': ") == "y":
                main_game()


main_game()
