MACHINE_GUN=0
RIFLE=1
SMG=2
AT=3
PISTOL=4
def get_input():
    fire_rate = input("Gun fire rate in rpm: ")
    weight = input("Gun weight in kg: ")
    capacity = input("Gun capacity in rounds: ")
    return Gun(int(fire_rate),int(weight),int(capacity))
def i_am(result):
    if (result[0] == MACHINE_GUN):
        print("I am a Machine gun")
    elif (result[0]) == RIFLE:
        print("I am a Rifle")
    elif (result[0]) == SMG:
        print("I am a SMG")
    elif (result[0]) == AT:
        print("I am an Anti Tank Gun")
    elif (result[0]) == PISTOL:
        print("I am a Pistol")
    else:
        print("I am unknown!")

class Gun:
 def __init__(self, fire_rate, weight,capacity):
     self.fire_rate = fire_rate
     self.weight = weight
     self.capacity = capacity
 def get(self):
     return [self.fire_rate,self.weight,self.capacity]
 def print(self):
     print("I am a gun with fire rate of %s with a weight of %s and an ammunition capacity of %s rounds" % (self.fire_rate, self.weight, self.capacity))
