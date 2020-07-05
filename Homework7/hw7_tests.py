from hw7_key import blitz, manualCount, replace
from hw7_data import blitz_matrix, count_matrix, replace_matrix

# blitz()
def testBlitz():
    succ = True
    testId = 1
    for x in blitz_matrix:
        if ( blitz(x[0]) != x[1] ):
            if(succ):
                print ("*blitz(): FAILED")
            print ("Test " + str(testId) + ") Expected: " + x[1] + "\n\tCalculated: " + blitz(x[0]))
            succ = False
        testId += 1
    if(succ):
        print ("blitz(): SUCCESSFUL")
        

# manualCount()
def testManualCount():
    succ = True
    testId = 1
    for x in count_matrix:
        if ( manualCount(x[0][0], x[0][1]) != x[1] ):
            if(succ):
                print ("*manualCount(): FAILED")
            print ("Test " + str(testId) + ") Expected: " + x[1] + "\n\tCalculated: " + manualCount(x[0][0], x[0][1]))
            succ = False
        testId += 1
    if(succ):
        print ("manualCount(): SUCCESSFUL")

# replace()
def testReplace():
    succ = True
    testId = 1
    for x in replace_matrix:
        if(replace(x[0][0], x[0][1], "&") != x[1]):
            if(succ):
                 print ("*replace(): FAILED")
            print ("Test " + str(testId) + ") Expected: " + x[1] + "\n\tCalculated: " + replace(x[0][0], x[0][1], "&") )
            succ = False
        testId += 1
    if(succ):
        print ("replace(): SUCCESSFUL")


print("*******************************************")
testBlitz()
testManualCount()
testReplace()
print("*******************************************")
