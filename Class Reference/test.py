# test.py
# Execution directions for testing items and backpacks
from Backpack import Backpack, Item

item = Item("Apple", True)
backpack = Backpack("Theo")

backpack.addItem(item)
backpack.addItem(item)

print(item)
print(backpack)