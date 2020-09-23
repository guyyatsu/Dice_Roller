import random

repeat = True #Sets us up with something to return _ to to restart the whole thing unless otherwise stated.
#More on that later.

while repeat == True: #The point at which we will return, unless otherwise stated of course.


    def dice_roller(): #Simulates a dice roll, the number of sides defined by the user.
        try: #Allows the the next three lines to accept invalid input from the user without breaking the program.
            dice = int(input('What sided die would you like to roll? ')) #Recieves numeric input that defines the upper limit to the randint() function.
            roll = random.randint(1, dice) #Generates a random number between 1 and whatever the value of dice is.
            print('You rolled a ' + str(roll) + '!') #Presents the result in a human-like way.

            """ Typically when the user inputs anything other than an integer, even including 0, the random library throws up an error.
                Try/Except creates a sort of unspoken loop that repeats only when the compiler would typically throw up an error.
                Otherwise, the script continues as usual with the user none the wiser."""

        except: 
            print('ERROR! Please only use valid integers. ')


    def do_over(): #Presents the user with the option to roll again if desired.
        error = False #As long as this remains False, the users input is valid and the script carries on as usual.
        while error == False: #Reverse Passive statement; if error ISN't True then nothing is wrong: carry on.
            asker = str.lower(input('Would you like to roll again? y/n: ')) #Recieves input, converts to lowercase, then checks for y or n.
            if asker == 'y': #If asker's value is yes, the loop is completed and restarts as usual.
                return repeat == True #Return allows you to interact with statements defined outside of the scope of the function.
            elif asker == 'n': #If asker's value is no, the program closes.
                return quit()
            else: #If asker isn't either y or n, initializes a pseudo-Try/Except function. 
                error == True 
                print('ERROR! Please input either Y or N!')


    dice_roller()
    do_over()