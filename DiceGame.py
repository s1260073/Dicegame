import random
class DiceGame():
    def __init__(self):
        self.roll()
    def roll(self):
        self.FaceValue=random.randint(1,6)
    def getFaceValue(self):
        return self.FaceValue
def play():
    print("what is your name?")
    name=input()
    print("Hello, "+name+"!")
    print("Rolling the dice... ")
    die1=DiceGame()
    die2=DiceGame()
    die3=DiceGame()
    fv1=die1.getFaceValue()
    fv2=die2.getFaceValue()
    fv3=die3.getFaceValue()
    print("Die 1:"+str(fv1))
    print("Die 2:"+str(fv2))
    print("Die 3:"+str(fv3))
    print("Total value:"+str(fv1+fv2+fv3))
    if(fv1+fv2+fv3>=7):
        print(name+" won")
    else:
        print(name+" lost")
    

play()

