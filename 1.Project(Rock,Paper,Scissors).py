import random
Rock='''       
------|
       |------|        
       -------|
       -------|
       -------|
       -----|
------ |
'''
Paper=''''
------|
       |-------|
       --------|
       -----------|
       -----------|
       ---------|
       |--------|
       |---|
-----------|

'''
Scissors='''
------|
       |--------|
       ---------|
       -------------|
       -------------|
       ----|
       ----|
       ----|
       ----|
------|       
'''
print("Hello guys,I think you doing good")
print("Now let's play the game")
print("*************************************")
print("Here are the 3 rules to follow,they are")
print("---------------------------------------")
print("Rock wins against Scissors")
print("Scissors wins aganist Paper")
print("Paper wins against Rock")
print("-----------------------------------------")
print("0.ROCK,1.PAPER,2.SCISSORS")
game_image=[Rock,Paper,Scissors]
uc=int(input("Enter your chocie "))
if uc>=3 or uc<0:
    print("Here your choice is invalid,please read the instructions")
else:
    print(game_image[uc])
    cc=random.randint(0,2)
    print("Here computer choice is :")
    print(game_image[cc])
    if cc==uc:
        print("Its a Draw,Play again")
    elif cc==0 and uc==2:
        print("You lose")
    elif uc==0 and cc==2:
        print("You win")
    elif cc>uc:
        print("You lose")
    elif uc>cc:
        print("You win")
print("Thanks for playing with me,Please would you play with me again")