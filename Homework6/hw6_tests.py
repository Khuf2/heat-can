from hw6_submission import blitz, getNthElement, formatName
from hw6_data import nth_matrix, name_matrix

# testSwap()
def testBlitz():
    if( blitz("D’endrrah") == "Welcome, D’endrrah. That was your blitz problem."):
        print ("blitz(): SUCCESSFUL")
    else: 
        print ("*blitz(): FAILED")
        print ("Expected: True     Calculated: " + blitz("D’endrrah"))
        

# getNthElement()
def testGetNthElement():
    succ = True
    testId = 1
    for x in nth_matrix:
        if ( getNthElement(x[0], x[1]) != x[1] ):
            print ("*getNthElement(): FAILED")
            print ("Test " + str(testId) + ") Expected: " + x[1] + "\n\tCalculated: " + getNthElement(x[0], x[1]))
            succ = False
        testId += 1
    if(succ):
        print ("getNthElement(): SUCCESSFUL")

# formatName()
def testFormatName():
    succ = True
    testId = 1
    for x in name_matrix:
        if(formatName(x[0][0], x[0][1], x[0][2]) != x[1]):
            print ("*formatName(): FAILED")
            print ("Test " + str(testId) + ") Expected: " + x[1] + "\n\tCalculated: " + formatName(x[0][0], x[0][1], x[0][2]) )
            succ = False
        testId += 1
    if(succ):
        print ("formatName(): SUCCESSFUL")


print("*******************************************")
testBlitz()
testGetNthElement()
testFormatName()
print("*******************************************")
