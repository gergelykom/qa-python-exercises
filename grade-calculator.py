maths = int(input('Please enter your maths mark: '))
chem = int(input('Please enter your chemistry mark: '))
phys = int(input('Please enter your physics mark: '))

result = round((maths + chem + phys) / 3, 2)

def grade():
    if result >= 70:
        return 'You scored a grade of: A'
    elif result >= 60:
        return 'You scored a grade of: B'
    elif result >= 50:
        return 'You scored a grade of: C'
    elif result >= 40:
        return 'You scored a grade of: D'
    else:
        return 'You failed'


print(result, '%', grade())