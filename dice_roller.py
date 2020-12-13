import random

repeat = True

while repeat == True:


    def dice_roller(how_many):
        dice_counter = True
        counter_tics = 0
        try:
            dice = int(input('What sided die would you like to roll? '))
        except:
            print('ERROR! Please only use valid integers. ')

        while counter_tics < int(how_many):
            roll = random.randint(1, dice)
            counter_tics += 1
            print('You rolled a ' + str(roll) + '!')
            if counter_tics == int(how_many):
                break

    def do_over():
        error = False
        while error == False:
            asker = str.lower(input('Would you like to roll again? y/n: '))
            if asker == 'y':
                return repeat == True
            elif asker == 'n':
                return quit()
            else:
                error == True 
                print('ERROR! Please input either Y or N!')


    dice_roller(input('How many dice would you like to roll? '))
    do_over()
