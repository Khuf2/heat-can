from hw2_submission import wordList, numList, mixedList, manualAbs, sumList, cutShort

# manualAbs()
def testManualAbs():
    tests = [40, -40, 0]
    bools = []
    for t in tests:
        bools.append(manualAbs(t) == abs(t))
    if ( all(bools) ):
        print ("manualAbs() test successful")
    else:

        for t in range( 0, len(tests) ):
            if ( tests[t] != abs(tests[t]) ):
                print ( "Test #" + str(t+1) + " failed. [num = " + str(tests[t]) + "]" )
        

# sumList()
def testSumList():
    if ( sumList(numList) == 16383 ):
        print ("sumList() test successful")
    else:
        print ("Expected: 16383     Calculated: " + sumList(numList))

# cutShort()
def testCutShort():
    if(cutShort(wordList, 3) != ['does', 'smell', 'like', 'burnt', 'toast', 'here']):
        print ("cutShort() test failed")
    else:
        print ("cutShort() test successful")

    # Bonus test
    if(cutShort(mixedList, 2) != ["going", "raise", 8, "baby", "geese"]):
        print ("cutShort() bonus test not passed")
    else:
        print ("cutShort() bonus test successful")

testManualAbs()
testSumList()
testCutShort()