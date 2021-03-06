# Homework 6 - 6/24/20
# Lists, String Building, String methods

# Terminal commands:
# python hw6_tests.py
# or 
# python hw6_submission.py

'''
# blitz(): basic string-building
Given a name, return a greeting message to the user in the form of a string. It should look like this:
# blitz("Hugo") = "Welcome, Hugo. That was your blitz problem."
# Hint: The link below is not necessary to this problem, but should be acknowledged for its utility in
        dealing with idiot-proofing user input. 
# https://www.w3schools.com/python/ref_string_strip.asp
'''
def blitz(name):
    # Your code starts here.
    return "Welcome, " + name.capitalize() + ". That was your blitz problem."

print ( blitz("Oli") )


'''
# getNthElement()
Given a list and an int n, return the n-th element in the list. n > 0.
# example_list = [4, 5, 6, 7, 8], n = 1 => 4
# example_list = [4, 5, 6, 7, 8], n = 5 => 8
Hint: n is slightly different than array index. ( example_list[n] is not equal to getNthElement(n) )
'''
def getNthElement(list, n):
    if (abs(n) > len(list)):
        return "Error"
    # Your code starts here.
    return list[n-1]
    
# test call = 5
print ( getNthElement([1, 2, 3, 4, 5], 5) )


'''
# formatName()
You are given strings for a first, middle, and last name.
Combine those strings to model this output:
# name = ["Theo", "Joseph", "Novak"]
# formatName(name[0], name[1], name[2]) = "Theodore J. Novak"
# Hint: This is similar to the blitz problem. A string is just an array of smaller 1-letter strings, so you can get
#       the first letter however you see fit. ( indexing or .slice() )
#       https://www.w3schools.com/python/gloss_python_string_slice.asp
'''
def formatName(first, mid, last):
    # Your code starts here.
    def myCap(word):
        # My custom capitalize method fixes the weird McDonald test case that .capitalize() messes up.
        x = word[0].upper()
        output = x + word[1:len(word)]
        return output

    fullName = myCap(first) + " " + mid[0].capitalize() + ". " + myCap(last)
    # Consider checking for the length of the middle name to avoid an indexing error if no
    # middle name was provided by a user. You also would not need the ". " in that case, and fullName
    # would evaluate to first.capitalize() + " " + last.capitalize()
    return ( fullName )


# Test call = Oliver R. Novak
print ( formatName("Oliver", "Richard", "Novak") )