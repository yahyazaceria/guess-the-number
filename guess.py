import random 
guesses = 1
num = random.randint(0,100)

guessed_num = int(input("Guess a number between 1 and 100: "))

while guessed_num != num:
  if guessed_num < num:
    print("Your number is too low.")  
    guessed_num = int(input("Guess another number: "))
    guesses = guesses + 1
  elif guessed_num > num:
    print("Your number is too high.")
    guessed_num = int(input("Guess another number: "))
    guesses = guesses + 1
    
    

print(f"You guessed it! You win! It took you {guesses} guesses to win. Good Job!")



 