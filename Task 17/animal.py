#Task 1
class Animal:
    def __init__(self, numteeth, spots, weight):
        self.numteeth = numteeth
        self.spots = spots
        self.weight = weight
    

    def __str__(self):
        return "Animal has {} of teeth, {} spots and {} kg".format(self.numteeth,self.spots,self.weight)


class Lion(Animal):
    def __init__(self, numteeth, spots, weight, sound, owner):
        self.owner = owner
        self.sound = sound
        super(Lion,self).__init__(numteeth, spots, weight)
        self.set_type()
    
    def set_type(self):
        if(self.weight < 80):
            return 'cub'
        elif(self.weight > 80 and self.weight < 120):
            return 'female'
        else:
            return  'Male'

    def __str__(self):
        lionType = self.set_type()
        return "Lion is {} kg, has {} teeths, type is {}, has {} spots and says {}. His owner is  {}".format(self.weight, self.numteeth, lionType, self.spots,self.sound,self.owner)

#Task 2
class Cheetah(Animal):

    def __init__(self, numteeth, spots, weight, survival):
        super(Cheetah, self).__init__(numteeth, spots, weight)
        self.survival = survival

    def __str__(self):
        return "Cheetah is {} kg, has {} teeths, and has {} spots \nFor survival it does the following: {}".format(self.weight, self.numteeth, self.spots, self.survival)

my_cheetah = Cheetah(28, "brown", 45, ["Hunt", "Sprint Faster", "Move in packs"])

print(my_cheetah)