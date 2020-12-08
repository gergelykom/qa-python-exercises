def checkcase():
    sentence = str(input('Enter your sentence: ')) #user input
    upper = 0 #number of uppercase
    lower = 0 #number of lowercase

    #loop through all letters -> add +1 to upper if uppercase, +1 to lower if lowercase
    for i in sentence:
        if i.isupper():
           upper+=1
        elif i.islower():
           lower+=1
    # returns as list?? numbers in str otherwise syntax error
    return sentence,"\nUPPER:",str(upper),"\nLOWER:",str(lower)
# turn list into str again
print(' '.join(checkcase()))