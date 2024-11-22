
set1 = {1, 2, 3}
set2 = {2, 3, 1}
print(set1 == set2)
print(set1 is set2)

set3 = set1
print(set1 == set3)
print(set1 is set3)
print()

set1 = {1, 2, 3}
set2 = {1, 2, 3}
print(set1 == set2)
print(set1 is set2)

print([1, 2, 3] == [2, 3, 1])
print('='*80)

s1 = {1, 2, 3}
s1.add('a')
s1.add(4.5)
print(s1)

s1.add(1)
print(s1)
print()

s1.remove(3)
print(s1)
print()

# s1.remove(3)
# print(s1)
# print()

s1.discard('a')
print(s1)
print()

s1.discard('a')
print(s1)
print()

x = s1.pop()
print(s1)
print(x)
print()

x = s1.pop()
print(s1)
print(x)
print()

x = s1.pop()
print(s1)
print(x)
print()

# x = s1.pop()
# print(s1)
# print(x)
# print()

print('='*80)

s2 = set('abc')
s3 = s2
s3.add('x')
print(hex(id(s2)), s2)
print(hex(id(s3)), s3)
print()

s3.clear()
print(hex(id(s2)), s2)
print(hex(id(s3)), s3)
print()

s1 = {2, 4.5}
s4 = s1.copy()
s4.add('z')
print(hex(id(s1)), s1)
print(hex(id(s4)), s4)
print()













