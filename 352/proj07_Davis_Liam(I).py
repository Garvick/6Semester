import random

def get_user_play():
    while True:
        command = input("Enter Rock, Paper, or Scissors: ").lower().strip()

        if command == "rock" or command == "paper" or command == "scissors":
            return command
        
        print("invalid option")
    
def getCompPick():
    choices = ("Rock", "Paper", "Scissors")
    return random.choice(choices)

#Returns to 1
def whoWins(userPick, compPick):
    if userPick == compPick:
        print("Tie game")
        return 0
    elif userPick == "rock" and compPick == "scissors":
        print("You win") 
        return 1
    elif userPick == "scissors" and compPick == "paper":
        print("You win")
        return 1
    elif userPick == "paper" and compPick == "rock":
        print("You win")
        return 1
    elif userPick == "scissors" and compPick == "rock":
        print("You loose")
        return -1
    elif userPick == "rock" and compPick == "paper":
        print("You loose")
        return -1
    elif userPick == "paper" and compPick == "scissors":
        print("You loose")
        return -1

userScore=0
compScore=0
while True:
    print("playing Rock, Paper, Scissors, Best 2 of 3")
    userPick = get_user_play()
    #print(userPick)
    compPick = getCompPick()
    print(f"Computer picked {compPick}")
    print(whoWins(userPick,compPick))
    score= whoWins(userPick, compPick)

    if score == 1:
        userScore += 1
    elif score ==-1:
        compScore += 1

    if userScore >=2:
        print("You have won!")
        break
    elif compScore >=2:
        print("Comp wins best 2 out of 3!")