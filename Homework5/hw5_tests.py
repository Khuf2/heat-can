from hw5_submission import blitz, printTri, golfScore

# testSwap()
def testBlitz():
    if( blitz() == True):
        print ("blitz() test successful")
    else: 
        print ("*blitz() test failed")
        print ("*Expected: True     Calculated: " + str(blitz()))
        

# manualReverse()
def testPrintTri():
    if ( printTri(4) == "*\n**\n***\n****\n" ):
        print ("printTri() test successful")
    else:
        print ("*printTri() test failed")
        print ("*Expected: \n*\n**\n***\n****\nCalculated: \n[" + printTri(4) + "]")

# manualReverse()
def testGolfScore():
    test_card = [ [4, 5, 5, 5, 3, 4, 3, 5, 4], [5, 4, 5, 6, 7, 4, 6, 4, 4] ]
    if(golfScore(test_card) != "+7"):
            print ("*golfScore() test failed")
            print ("*Expected: +7       Calculated: \n[" + golfScore(test_card) + "]")
    else:
        print ("golfScore() test successful")


print("*******************************************")
testBlitz()
testPrintTri()
testGolfScore()
print("*******************************************")
