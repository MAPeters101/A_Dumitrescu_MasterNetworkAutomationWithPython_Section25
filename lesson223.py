
s1 = {1, 2, 3, 'a', 'b', 4}
print(s1)
print(s1)
print(s1)
print(s1)
print(s1)
#print(s1[0])
print()

s1 = {1, 2, 3, 'a', 'b', 4, 1, 2, 'a', 3, 10}
print(s1)
s1.add((10, 20))
print(s1)
s1.remove('a')
print(s1)
print()

l1 = [1, 2]
#s1.add(l1)

s2 = set()
print(s2)

s3 = {}
print(type(s3))
print()

s4 = set('helloooooo!!!')
print(s4)

s5 = set((1, 2, 3, 4, 'abc'))
print(s5)

l2 = [10, 20, 30, 40]
print(set(l2))

macs = ['30-24-32-E2-0F-59', '30-24-32-E2-0F-59', '30-24-32-E2-0F-59',
        '30-24-32-E2-0F-59', '30-24-32-E2-0F-59', '30-24-32-E2-0F-60']
mac_addresses = set(macs)
print(mac_addresses)
print(len(mac_addresses))
print()

mac_addresses = list(set(macs))
print(mac_addresses)
print(len(mac_addresses))
print()


for item in s4:
    print(item)
print()

print('x' in s4)




