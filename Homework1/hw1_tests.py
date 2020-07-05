from hw1_submission import removeAll, smartAdd, getMin

list = [10, 30, 40, 35, 65, 25, 40, 85, 105, 55, 55]

# removeAll()
def testRemoveAll():
    removeAll(40)
    if(list.count(40) != 0):
        print ("removeAll() test failed")
    else:
        print ("removeAll() test successful")

# smartAdd()
def testSmartAdd():
    smartAdd(85)
    smartAdd(80)
    if((list.count(85) > 1) or (list.count(80) != 1)):
        print ("smartAdd() test failed")
    else:
        print ("smartAdd() test successful")

# getMin()
def testGetMin():
    if(getMin() != 10):
        print ("getMin() test failed")
    else:
        print ("getMin() test successful")

testRemoveAll()
testSmartAdd()
testGetMin()
