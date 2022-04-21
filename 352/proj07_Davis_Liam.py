import random
#list of choices
rosh_list= ["rock", "paper","scissors"]
#setup for classes
class player:
    def __init(self,name):
        self.name=name
        self.roshchoice=""

class Bart(player):
    def __init__(self):
        player. __init__(self,"Bart")
    def generateRoshambo(self):
        self.roshchoice = rosh_list[0]

class Lisa(player):
    def __init__(self):
        player. __init__(self,"Lisa")
    def generateRoshambo(self):
        self.roshchoice = rosh_list[random]

def main():
    print("Roshambo Game")/n
    playername= input("Enter your name: ")/n
        player1=player(playername)
        opponet= input("Would you like to play Bart or Lisa? (b/l): ").lower
        if b:
            player2=Bart()
        else l:
            player2=Lisa()
    input("Rock, paper, scissors r/p/s: ").lower/n
    if player1.roshchoice=

    player2.generateRoshambo():

    playgame(player1,player2)

    if player1.roshchoice==player2.roshchoice:
        retrun Draw