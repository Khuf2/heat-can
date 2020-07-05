# Homework 1 - 6/17/20
# Lists, Conditionals, Variables, Loops
# Indexes, List Methods :: https://www.w3schools.com/python/python_ref_list.asp


# The list you will use for your testing is this one here:

list = [10, 30, 40, 35, 65, 25, 40, 85, 105, 55, 55]


# (Easy) Write the code for two functions, removeAll() and smartAdd().

# removeAll()
# Removes all instances of an element from a list, or 
# does nothing if the element isn't there.
def removeAll(e):
    # Your code starts here. e is like x from lesson, the element you are removing.
    while (list.count(e) > 0):
        list.remove(e)
    # Done



# smartAdd() will add a new element to the back of a list, but 
# will do nothing if the  element already exists in the list. (i.e. no duplicates)
def smartAdd(e):
    # Your code starts here
    if(list.count(e) == 0):
        list.append(e)
    # else:
        # Do nothing (therefore this is unnecessary)
    # Done


# (Medium) Write the code for the function, getMin().

# getMin()
# Finds and returns the lowest numerical value in the list.
def getMin():
    # Your code starts here
    min = None
    for e in list:
        if ((min == None) or (min > e)):
            min = e
    return (min)
    # Done
