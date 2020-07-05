# Homework 8 - 6/30/20
# Dictionaries and helper methods, slow intro to objects

'''
# blitz(): accessing a value in a dictionary
Given a dictionary called person, return the 'name' field from person. It is a key in the person dictionary. 
# blitz({"name": "Dante", "hair": "Umber", "height": "186 cm"}) = "Dante"
'''
def blitz(person):
    # Your code starts here.
    return person["name"]

# test call = "Waldo"
print ( blitz({"name": "Waldo", "hair": "Black", "height": "192 cm"}) )


'''
# buildDictionary()
Given a list of terms and a list of definitions, whose values at index 0-n correspond to each other as (term/definition pairs).
Combine these two lists into a dictionary, with the terms being the keys, and the defs the values.

'''
def buildDictionary(terms, defs):
    # Your code starts here.
    if(len(terms) is not len(defs)):
        return "error"
    dict = {}
    for x in range(0, len(terms)):
        dict[terms[x]] = defs[x]
    return dict
    


# Test call = {'mald': 'To be very upset, scalding mad. Hence, mald.', 'instigate': 'incite someone to do something, especially something bad.', 'chones': 'underwear, slangily.'}
terms = ["mald", "instigate", "chones"]
definitions = ["To be very upset, scalding mad. Hence, mald.", "incite someone to do something, especially something bad.", "underwear, slangily."]
print ( buildDictionary(terms, definitions) )


'''
# findOldest()
Given a list of dictionaries called people, where each dictionary represents a person,
return the oldest person. This can be found via the age field in each person dictionary. 
Complete the getAge() helper function and use it in your answer.
'''
def findOldest(people):
    # Your code starts here.
    if(len(people) == 0):
        return None
    
    def getAge(person):
        # make this helper function (like your blitz)
        return person["age"]
    
    oldest = people[0]
    for x in people[1:]:
        if getAge(x) > getAge(oldest):
            oldest = x
    return oldest
    
# test call = "{"name": "TJ Lavin", "hair": "Mullet", "age": 43}"
persons = [
    {"name": "Waldo", "hair": "Black", "age": 29}, 
    {"name": "Scarra", "hair": "Barely", "age": 30}, 
    {"name": "Devin", "picture": "baseball.png", "mald": True, "age": 13}, 
    {"name": "Bruno Mars", "hair": "Black", "age": 34}, 
    {"name": "TJ Lavin", "hair": "Mullet", "age": 43}
]
print ( findOldest(persons) )