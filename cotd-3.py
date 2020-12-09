def zipping():
    str1 = str(input('Enter your first sentence:')) #first str
    str2 = str(input('Enter your second sentence:')) #second str
    together = '' #empty var 2 hold final str
    for i in zip(str1,str2): #loop through zipped var's
        together += ''.join(i) #turn tuple back to str



    return together


print(zipping())




