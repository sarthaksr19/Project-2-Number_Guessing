import random
randnumber = random.randint(1,100)

userGuess = None
guesses = 0

while(userGuess != randnumber):
    userGuess = int(input("Enter Your Guess: "))
    guesses += 1
    if(userGuess == randnumber):
        print("You Guessed it Right!!!")
    elif(userGuess > randnumber):
        print("You Guessed it wrong! please Enter a Samller Number")
    elif(userGuess < randnumber):
        print("You Guessed it wrong! Please Enter a Greater Number")

print(f"You Guessed the Right Number in {guesses} Attempt.")


## Storing a hiscore one who makes a least number of guesses.
with open("hiScore.txt") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print("Congratulations! You have just broken the Hi Score")
    with open("hiScore.txt","w") as f:
        f.write(str(guesses))
    
