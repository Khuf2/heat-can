from hw8_submission import blitz, buildDictionary, findOldest

# blitz()
def testBlitz():
    person = {"name": "Nut Zach"}
    if(blitz(person) == "Nut Zach"):
        print ("blitz(): SUCCESSFUL")
    else:
        print ("*blitz(): FAILED")
        print ("\tExpected: " + person["name"] + "\n\tCalculated: " + blitz(person))
        

# buildDictionary()
def testBuildDictionary():
    terms = ["divulge", "chunk"]
    defs = ["make known (private or sensitive information).", "a thick, solid piece of something."]
    exDict = {"divulge": "make known (private or sensitive information).", "chunk": "a thick, solid piece of something."}
    if(buildDictionary(terms, defs) == exDict):
        print ("buildDictionary(): SUCCESSFUL")
    else:
        print ("*buildDictionary(): FAILED")
        print ("\tExpected: " + str(exDict) + "\n\tCalculated: " + buildDictionary(terms, defs))

# findOldest()
def testFindOldest():
    nz = {"name": "Nut Zach", "age": 33}
    chuck = {"name": "Charles Barkley", "age": 57}
    people = [nz, chuck]
    if(findOldest(people) == chuck):
        print ("findOldest(): SUCCESSFUL")
    else:
        print ("*findOldest(): FAILED")
        print ("\tExpected: " + str(chuck) + "\n\tCalculated: " + findOldest(people))


print("*******************************************")
testBlitz()
testBuildDictionary()
testFindOldest()
print("*******************************************")
