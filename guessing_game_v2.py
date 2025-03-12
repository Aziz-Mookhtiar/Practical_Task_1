def main():
    from random import randint

    print ("In this program you will enter a number between 1 - 100."
        "\nAfter the computer will try to guess your number!")

    number = 0

    while number < 1 or number >200:
        number = int(input("\n\nEnter a number for the computer to guess: "))
        if number > 100:
            print ("Number must be lower than or equal to 200!")
        if number < 1:
            print ("Number must be greater than or equal to 1!")


    guess=0
    print("")
    print("the computer is gusseing your number....")
    print("")
    while True:
        guess +=1
        random_guess = randint(1, 100)
        print (random_guess)
        if  guess <= 9 and random_guess == number:
            print("")
            print ("It took the computer ",guess, " guesses to find your number")
            print("")
            print ("The computer guessed", guess, " this many times")
            break
            
        elif guess >9:
            print("I could not guess your number..")
            restart= input("Do you wanna retry? Y/N....")
            if restart == "Y":
                main()
            
main()

           
            


        
       
        
   



   



    

            
