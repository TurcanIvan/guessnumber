## number guessing game 0..9
import random 

number = random.randint (0,9)


# LOOP - 5 trials
for trials in range(5):

    n =  int(input("Guess the number (0..9 ) >> "))

    if n == number:
        print("You win !!!")
    else:
        print("Wrong !!!")

        if n > number:
            print("hint: Try lower ;)")
        if n < number:
            print("hint: Try higher ;)")        
