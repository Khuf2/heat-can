# Copy and paste test code into your python window after your completed functions. It will run and print a 
# message indicating whether you passed or not. :)

from hw4_submission import blitz, printBox, checkMatrix
from hw4_data import matrix


# testSwap()
def testBlitz():
    if( blitz() == ['waited', 'exited', 'breaked', 'createed', 'seemed', 'controled', 'booled', 'cooked']):
        print ("blitz() test successful")
    else: 
        print ("*blitz() test failed")
        print ("*Expected: ['waited', 'exited', 'breaked', 'createed', 'seemed', 'controled', 'booled', 'cooked']     Calculated: [" + ', '.join((str(v) for v in (blitz()))) + "]")
        

# manualReverse()
def testPrintBox():
    if ( printBox(4, 5) == "*****\n*****\n*****\n*****\n" ):
        print ("printBox() test successful")
    else:
        print ("*printBox() test failed")
        print ("*Expected: \n*****\n*****\n*****\n*****\n      Calculated: \n[" + printBox(4, 5) + "]")

# manualReverse()
def testCheckMatrix():
    fail = False
    for test in range(0, len(matrix)):
        if(checkMatrix(matrix[test][0]) != matrix[test][1]):
            print ("*checkMatrix() test failed")
            print ("*Expected: " + str(matrix[test][1]) + "      Calculated: \n[" + str(checkMatrix(matrix[test][0])) + "]")
    if(not fail):
        print ("checkMatrix() test successful")


print("*******************************************")
testBlitz()
testPrintBox()
testCheckMatrix()
print("*******************************************")
