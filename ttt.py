#INTRODUCING GAME TO USER
from random import randint
print("WELCOME TO THE GAME!")

print('\nHere are the gaming instructions\n1. The game is you vs computer\n2. You will enter a number from 1 to 9 representing the following positions:\n\t1\t2\t3\n\t4\t5\t6\n\t7\t8\t9\n3.You will insert your "X" or "O" in your desired position followed by the computer\n4.To win, the "X" or the "O" need to form a line horizontally, vertically or diagonally\n5.To win, the "X" or the "O" need to form a line horizontally, vertically or diagonally')

print("\nGOODLUCK.")

#USER GAMEPLAY

user_selection=input('Pick "X" or "O" ').upper()
from random import randint
count=1
template_position="\n\t1\t2\t3\n\t4\t5\t6\n\t7\t8\t9"
game_finish = False
while count<=9 :
    if user_selection=="X" and count%2!=0:
        print("YOUR TURN")
        pos=input("Enter position ")
        new_pos=template_position.replace(pos,"X")
        count+=1
        template_position=new_pos
        print(template_position)
        checking_temp = repr(template_position)
    elif user_selection=="O" and count%2!=0:
        print("YOUR TURN")
        pos=input("Enter position")
        new_pos=template_position.replace(pos,"O")
        template_position=new_pos
        count+=1
        print(template_position)
        checking_temp = repr(template_position)


#COMPUTER'S GAME PLAY

    if user_selection=="X" and count%2==0:
        print("COMPUTER'S TURN")
        pos1=randint(1,9)
        while not str(pos1) in template_position:
            pos1 = randint(1,9)
        new_pos1=template_position.replace(str(pos1),"O")
        count+=1
        template_position=new_pos1
        print(template_position)
        checking_temp = repr(template_position)
    elif user_selection=="O" and count%2==0:
        print("COMPUTER'S TURN")
        pos1=randint(1,9)
        while not str(pos1) in template_position:
            pos1 = randint(1,9)
        new_pos1=template_position.replace(str(pos1),"X")
        count+=1
        template_position=new_pos1
        print(template_position)
   

        checking_temp = repr(template_position)
   
    #TERMINATION OF WHILE LOOP

    if (checking_temp[5] == checking_temp[8] == checking_temp[11] == "X" or checking_temp[16] == checking_temp[19] == checking_temp[22] == "X" or checking_temp[27] == checking_temp[30] == checking_temp[33] == "X" or checking_temp[5] == checking_temp[16] == checking_temp[27] == "X" or checking_temp[8] == checking_temp[19] == checking_temp[30] == "X" or checking_temp[11] == checking_temp[22] == checking_temp[33] == "X" or checking_temp[11] == checking_temp[19] == checking_temp[27] == "X" or checking_temp[5] == checking_temp[19] == checking_temp[33] == "X") and user_selection == "X":
        print("YOU WON, YAY!")
        game_finish = True
        break
    elif (checking_temp[5] == checking_temp[8] == checking_temp[11] == "O" or checking_temp[16] == checking_temp[19] == checking_temp[22] == "O" or checking_temp[27] == checking_temp[30] == checking_temp[33] == "O" or checking_temp[5] == checking_temp[16] == checking_temp[27] == "O" or checking_temp[8] == checking_temp[19] == checking_temp[30] == "O" or checking_temp[11] == checking_temp[22] == checking_temp[33] == "O" or checking_temp[11] == checking_temp[19] == checking_temp[27] == "O" or checking_temp[5] == checking_temp[19] == checking_temp[33] == "O") and user_selection == "X":
        print("YOU LOSE, BOO!")
        game_finish = True
        break
    elif (checking_temp[5] == checking_temp[8] == checking_temp[11] == "X" or checking_temp[16] == checking_temp[19] == checking_temp[22] == "X" or checking_temp[27] == checking_temp[30] == checking_temp[33] == "X" or checking_temp[5] == checking_temp[16] == checking_temp[27] == "X" or checking_temp[8] == checking_temp[19] == checking_temp[30] == "X" or checking_temp[11] == checking_temp[22] == checking_temp[33] == "X" or checking_temp[11] == checking_temp[19] == checking_temp[27] == "X" or checking_temp[5] == checking_temp[19] == checking_temp[33] == "X") and user_selection == "O":
        print("YOU LOSE, BOO!")
        game_finish = True
        break
    elif (checking_temp[5] == checking_temp[8] == checking_temp[11] == "O" or checking_temp[16] == checking_temp[19] == checking_temp[22] == "O" or checking_temp[27] == checking_temp[30] == checking_temp[33] == "O" or checking_temp[5] == checking_temp[16] == checking_temp[27] == "O" or checking_temp[8] == checking_temp[19] == checking_temp[30] == "O" or checking_temp[11] == checking_temp[22] == checking_temp[33] == "O" or checking_temp[11] == checking_temp[19] == checking_temp[27] == "O" or checking_temp[5] == checking_temp[19] == checking_temp[33] == "O") and user_selection == "O":
        print("YOU WON, YAY!")
        game_finish = True
        break
    
if count == 9 and game_finish == False:
    print("GAME TIE!")
