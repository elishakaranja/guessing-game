import random

def guess_number():
    while True:
        # Generate a random number between 1 and 50
        number_to_guess = random.randint(1, 50)
        attempts = 0 

        while True:
            try:
                # Get user input and track attempts
                guess = int(input("Guess a number between 1 and 50: "))
                attempts += 1 

                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
                    break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # ask if user wants to play again 
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    guess_number()
