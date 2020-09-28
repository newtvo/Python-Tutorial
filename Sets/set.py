# set content
s = {1, 3, 2, 'hello', 2}
print(s)

# convert list to set
a = [1, 2, 1, 3]
s = set(a)
print(s)
print(type(s))

# set operations
# add
s = {1, 2, 3}
s.add('hello')
print(s)

# remove
s.remove('hello')
print(s)

# verification
print((1 in s))

# set logic operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1.intersection(s2))

print(s1.union(s2))
print(s1.difference(s2))

print(set([4]).issubset(s2))
print(set([3, 4, 6, 5]).issuperset(s2))