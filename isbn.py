isbn = [int(i) for i in input('Please enter ISBN: ')]
isbn[12] = 10 -((isbn[0] + (3 * isbn[1]) + isbn[2] + (3 * isbn[3]) + isbn[4] + (3 * isbn[5]) + isbn[6] + (3 * isbn[7]) + isbn[8] +( 3 * isbn[9]) + isbn[10] + (3 * isbn[11])) % 10)

isbnstr = [str(x) for x in isbn]


isbnstr2 = ''.join(isbnstr)
isbn2 = int(isbnstr2)



print(isbnstr2[0:3], '-',isbnstr2[3:4], '-', isbnstr2[4:7], '-',isbnstr2[7:11], '-',isbnstr2[12])