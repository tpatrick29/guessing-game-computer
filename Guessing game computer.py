#Guessing game computer


def main():
    import random   
    import math

    lowest_Num = 1 #poss 0?
    highest_Num = 1000
    possible_Guess = highest_Num + lowest_Num - 1
    maxTurns = (math.log2(possible_Guess) + 1)
    your_Guess = int()
    playerAAnswer = ''
    turn_Count = 1 #poss 0?

    print(f'Choose a number from {lowest_Num} to {highest_Num}')
    print(f'I will guess your number in {maxTurns} turns or less!')
    input("Press Enter when you're ready.")

    while True:
        #/////////////////////begin loop///////////////////////
        possible_Guess = highest_Num + lowest_Num - 1
        your_Guess = math.ceil(possible_Guess / 2.0)

        print(f'Is your number {your_Guess}?\n')
        playerAAnswer = int(input("Press (1)Yes (2)Guess a lower number (3)Guess a higher number\n"))

        if playerAAnswer not in range(1,4):
            raise Exception("I get it you're slick, push the 1 the 2 or the 3 key my dude.")
        else:
            playerAAnswer = playerAAnswer

        if playerAAnswer == 3:
            lowest_Num = your_Guess + 1
        if playerAAnswer == 2:
            highest_Num = your_Guess - 1
        if playerAAnswer == 1:
            print('Got em')
            break   
        #//////////////////End of loop////////////////////
        turn_Count += 1

    while playerAAnswer == 1:
        print(f'I guessed your number in {turn_Count} turns! goober.\n')
        break


main()

