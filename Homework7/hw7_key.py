# Homework 7 - 6/25/20
# Lists, String Building, String Slicing, For Loop Review

'''
# blitz(): basic string-building from a list
Given a list of names, return a greeting message to each name in the form of a string.
If addressing more than one person, add an and to your final welcome, and adjust capitalization accordingly.
It should look like this:
# blitz(["Aldo", "Beto", "Carlo"]) = "Welcome, Aldo. Welcome, Beto. And welcome, Carlo."
# blitz(["Arty"]) = "Welcome, Arty."
'''
def blitz(names):
    # Your code starts here.
    output = ""
    for index in range(0, len(names)):
        if index != (len(names)-1) or index == 0:
            output += "Welcome, " + names[index] + "."
            if len(names) != 1:
                output += " "
        else:
            output += "And welcome, " + names[index] + "."
    return output
        

print ( blitz(["Aldo", "Beto", "Carlo"]) )


'''
# manualCount()
Given a string (text), a target string (word), return an int 
that equals how many times (word) appears in (text).

'''
def manualCount(text, word):
    # Your code starts here.
    count = 0
    i = 0
    while (i < len(text)):
        chunk = text[i: i+len(word)]
        if chunk == word:
            count += 1
            i += len(word)
        else:
            i += 1
    return count


# Test call = 2
print ( manualCount("Hoot Hoot Smoot Loot I Shoot Big Frisbees (1825) ##$ - Syrup", "Hoot") )


'''
# replace()
Given a string (text), a target string (word), and a replacement string (rep), 
return a new string with all instances of (word) replaced with (rep).
Hint: This is very similar to the last problem
'''
def replace(text, word, rep):
    # Your code starts here.
    output = ""
    i = 0
    while (i < len(text)):
        chunk = text[i: i+len(word)]
        if chunk == word:
            output += rep
            i += len(word)
        else:
            output += text[i]
            i += 1
    return output
    
# test call = "No No No No Smoot Loot I Shoot Big Frisbees (1825) ##$ - Syrup"
print ( replace("Hoot Hoot Smoot Loot I Shoot Big Frisbees (1825) ##$ - Syrup", "Hoot", "No No") )