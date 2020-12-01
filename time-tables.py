num = int(input('Please enter your number: '))

def tables(num):
    for top in range(1, num + 1):
        for down in range(1, num +1):
            print(top * down, end='\t')
        print()

tables(num)