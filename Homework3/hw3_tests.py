# Copy and paste test code into your python window after your completed functions. It will run and print a 
# message indicating whether you passed or not. :)

from hw3_submission import list, swap, manualReverse


# testSwap()
def testSwap(list):
    swap(list, 0, 3)
    swap(list, 3, 4)
    swap(list, 1, 0)
    if( list == [4, 8, 6, 10, 2]):
        print ("swap() test successful")
    else: 
        print ("*swap() test failed")
        print ("*Expected: [4, 8, 6, 10, 2]     Calculated: [" + ', '.join((str(v) for v in (list))) + "]")
        

# manualReverse()
def testManualReverse(list):
    mylist = [2, 4, 6, 8, 10]
    if ( manualReverse(mylist) == [10, 8, 6, 4, 2] ):
        print ("manualReverse() test successful")
    else:
        print ("*manualReverse() test failed")
        print ("*Expected: [10, 8, 6, 4, 2]      Calculated: [" + ', '.join((str(v) for v in (mylist))) + "]")


print("*******************************************")
testSwap(list)
testManualReverse(list)
print("*******************************************")
