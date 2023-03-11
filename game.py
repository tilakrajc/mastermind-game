import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'P']        # Red, Green, Blue, Yellow, White, Purple
TRIES = 10                                     # Number of tries
CODE_LENGTH = 4                                # Length of code

def generate_code():                           # Generate a random code
    return [random.choice(COLORS) for i in range(CODE_LENGTH)]

def get_guess():                               # Get a guess from the user
    guess = input("Enter your guess: ").upper().strip().split(" ")
    if len(guess) != CODE_LENGTH:              # Check if the guess is the correct length
        print(f"Invalid guess, must be {CODE_LENGTH} colors, guess again")
        return get_guess()
    
    for color in guess:                        # Check if the guess is valid
        if color not in COLORS:
            print(f"Invalid guess, {color} is not a valid color, guess again")
            return get_guess()
        
    return guess   # Return the guess as a list

def check_guess(guess, code):                 # Check if the guess is correct
    
    color_count = {}                          # Dictionary to count the number of each color in the guess
    correct_pos = 0                           # Number of correct positions
    incorrect_pos = 0                         # Number of incorrect positions
    for color in guess:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for guess_color, real_color in zip(guess, code):
        if guess_color == real_color:
            color_count[guess_color] -= 1
            correct_pos += 1
    
    for guess_color, real_color in zip(guess, code):
        if guess_color != real_color and real_color in color_count and color_count[real_color] > 0:
            color_count[real_color] -= 1
            incorrect_pos += 1

    return correct_pos, incorrect_pos


def game(): 
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code")
    print(f"The code is {CODE_LENGTH} colors long, and the colors are {', '.join(COLORS)}")

    code = generate_code()
    print(f"Code: {code}")                # Print the code for testing
    for attempts in range(1,TRIES+1):
        guess = get_guess()
        correct_pos, incorrect_pos = check_guess(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} attempts")
            break

        print(f"Correct positions: {correct_pos}, Incorrect positions: {incorrect_pos}")
    else:
        print(f"You ran out of attempts, the code was {code}")


if __name__ == "__main__":
    game()