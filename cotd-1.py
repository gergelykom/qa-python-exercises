def sentence():
    # enter input
    stuff = str(input('Please enter your sentence: '))

    # create a list so str can be sorted
    stuff2 = stuff.split()

    # turn into set(no duplicates) -> sort alphabetically -> turn into str with join, 1 space between
    print (" ".join(sorted(set(stuff2))))



sentence()
