# You have to use a random choice function to select snake, water, and gun.
# You do not have to use a print statement in case of the above function.
# Then you have to give input from your side.
# After getting ten consecutive inputs, the computer will show the result based on each iteration.
# You have to use loops(while loop is preferred).


print("                                        SNAKE WATER GUN GAME")

import random

print("How many rounds you want to play")
rounds_numbers = int(input())

print("g for gun\n"
      "s for snake\n"
      "w for water\n")

pc_point = 0

your_point = 0

i = 1

while(i<=rounds_numbers):
    print("Round" ,i)
    pc_choice = ["[snake]", "[water]", "[gun]"]
    pc_moves = random.choice(pc_choice)

    print("your moves")
    user_move = input()

    print("computer moves", pc_moves)

    if user_move == "s":
        if pc_moves == "[snake]":
            print("DRAW")
            print("your point is", your_point, "and computer point is", pc_point)
        elif pc_moves == "[water]":
            print("YOU WIN")
            your_point+=1
            print("your point is" ,your_point , "and computer point is" , pc_point)
        elif pc_moves == "[gun]":
            print("YOU LOOSE")
            pc_point+=1
            print("your point is", your_point, "and computer point is", pc_point)
    elif user_move == "w":
        if pc_moves == "[water]":
            print("DRAW")
            print("your point is", your_point, "and computer point is", pc_point)
        elif pc_moves == "[gun]":
            print("YOU WIN")
            your_point+=1
            print("your point is", your_point, "and computer point is", pc_point)
        elif pc_moves == "[snake]":
            pc_point+=1
            print("your point is", your_point, "and computer point is", pc_point)
            print("YOU LOOSE")
    elif user_move == "g":
        if pc_moves == "[gun]":
            print("DRAW")
            print("your point is", your_point, "and computer point is", pc_point)
        elif pc_moves == "[snake]":
            print("YOU WIN")
            your_point+=1
            print("your point is", your_point, "and computer point is", pc_point)
        elif pc_moves == "[water]":
            print("YOU LOOSE")
            pc_point+=1
            print("your point is", your_point, "and computer point is", pc_point)
    else:
        print("you entered wrong input")
    if i == rounds_numbers:
        print("                                             GAME OVER!!")
    i+=1
    print()

print("Your Final points\n",your_point , "\nand computer final points\n",pc_point)