MACHINE_GUN=0
RIFLE=1
SMG=2
def get_input():
    fire_rate = input("Gun fire rate in rpm: ")
    weight = input("Gun weight in kg: ")
    return Gun(int(fire_rate),int(weight))
def i_am(result):
    if (result[0] == MACHINE_GUN):
        print("I am a machine gun")
    elif (result[0]) == RIFLE:
        print("I am a rifle")
    elif (result[0]) == SMG:
        print("I am a SMG")
    else:
        print("I am unknown!")

class Gun:
 def __init__(self, fire_rate, weight):
     self.fire_rate = fire_rate
     self.weight = weight
 def get(self):
     return [self.fire_rate,self.weight]
 def print(self):
     print("I am a gun with fire rate of %s with a weight of %s" % (self.fire_rate, self.weight))
