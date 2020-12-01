def neartest():
    near1 = str(input('Word1: '))
    near2 = str(input('Word2: '))


    near = ''
    nearer = ''

    lengt = len(near2) if len(near1)<len(near2) else len(near1)

    for i in range(lengt):
        word1 = near1[i:i + 1]
        word2 = near2[i:i+1]
        if word1 != word2:
            near += word1
            nearer += word2

    if len(near) + len(nearer) <= 3:
        print('True', near1, near2)
    else:
        print('False')

neartest()


