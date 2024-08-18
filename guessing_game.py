import random 

#guess number between 1 qnd 100
def guess_number():
    number_to_guess = random.randint(1,100)
    attempts = 0 
    
    #create a loop to take in user input 
    while True:
        try:
            guess = int(input("guess number between 1 and 100"))
            attempts += 1 
        
            if guess < number_to_guess:
             print("Too low!")
            elif guess > number_to_guess:
             print("Too high!")
            else:
             print("Congratulations you guessed the correct number!")
             
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    
    guess_number()
            
        
        
        
         
    
    