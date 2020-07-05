# Backpack.py includes both Backpack AND Item classes

# Backpack - Backpack object holds items and belongs to a person.

class Backpack:
    def __init__(self, owner, capacity=10):
        self.slots = []
        self.owner = owner[0].upper() + owner[1:]
        self.capacity = capacity

    # this is a 'getter'
    def getOwner(self):
        return self.owner
    
    # this is a 'getter'
    def getCapacity(self):
        return self.capacity

    def getFullSlots(self):
        return len(self.slots)

    # this is a 'setter'
    def increaseCap(self, amt):
        self.capacity += amt

    def checkAdd(self, name):
        for x in self.slots:
            if(x.getName() == name):
                return x
        return None


    def addItem(self, item):
        if(len(self.slots) >= self.capacity):
            print ("No more inventory space.")
        else:
            stackTo = self.checkAdd(item.getName())
            if(stackTo == None):
                self.slots.append(item)
                print("Successfully picked up " + item.getName()  + " (x" + str(item.getCount()) + ").")
            else:
                stackTo.setCount(stackTo.getCount()+item.getCount())
                print("Successfully stacked " + item.getName()  + " (x" + str(item.getCount()) + ").")

    # this is the 'toString()'
    def __str__(self):
        output = "\n" + self.owner + "'s Inventory: (" + str(self.getFullSlots()) + "/" + str(self.getCapacity()) + ")\n"
        for item in self.slots:
            output += "\t" + str(item) + "\n"
        return output


# Item - Item object contains data about the "drop" or "weapon".
class Item:
    def __init__(self, name, stackability, count=1):
        self.name = name[0].upper() + name[1:]
        self.count = count
        self.stackable = stackability
    
    # this is a 'getter'
    def getStackable(self):
        return self.stackable

    # this is a 'getter'
    def getName(self):
        return self.name
    
    def getCount(self):
        return self.count

    def setCount(self, val):
        self.count = val
    
    # this is the 'toString()'
    def __str__(self):
        output = self.name + "\tx" + str(self.count)
        return output