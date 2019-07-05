import random
class DiceGame():
    def __init__(self):
        self.roll()
    def roll(self):
        self.FaceValue=random.randint(1,6)
    def getFaceValue(self):
        return self.FaceValue
def play():
    print("Rolling the dice... ")
    die1=DiceGame()
    die2=DiceGame()
    fv1=die1.getFaceValue()
    fv2=die2.getFaceValue()
    print("Die 1:"+str(fv1))
    print("Die 2:"+str(fv2))
    print("Total value:"+str(fv1+fv2))
    

play()

