
set1 = {1, 3, 5}
set2 = {5, 7, 9}

# 1. set.intersection()
set3 = set1.intersection(set2)
print(f'{set3=}')

set3 = set1 & set2
print(f'{set3=}')
print()


# 1. set.difference()
set4 = set1.difference(set2)
print(f'{set4=}')

set4 = set1 - set2
print(f'{set4=}')
print()

set4 = set1.difference([1, 2, 4, 5])
print(f'{set4=}')

# set4 = set1 - [1, 2, 4, 5]
set4 = set1 - set([1, 2, 4, 5])
print(f'{set4=}')
print()

set4 = set2.difference(set1)
print(f'{set4=}')

set4 = set2 - set1
print(f'{set4=}')
print()



