# indexing - use square bracket when create lists
a = ['hello', 1, 32, 1]
print(len(a))
print(type(a))
print(a[0])
print(a[-1]) # phần tử cuối cùng - index
print(a[-2])

# list content - can be string, tuple, integers
b = [1, 2, 'hello', (2, 'tuple'), [4, 5, 6]]
print(type(b))
print(type(b[3]))
print(b[4][2])

# list operations
c = ['hello', 3, 4, (3, 'tuple'), [3, 9, 0]]
c.extend([99, 'extend']) # add vao 3 phan tu
c.append([0, 9, 5]) # add vao 1 phan tu
print(type(c))
print(c[0])
print(c)
c[0] = 999
print(c)
del(c[0])
print(c)

s = 'a, b, c, d'
print(type(s))
d = s.split(',')
print(type(d))


# copy and clone list
m = [1, 2, 'list']
n = m # copy
print(m)
print(n)
m[0] = 999
print(m)
print(n)

n = m[:] # clone - mang moi hoan toa
print(m)
print(n)

m[0] = 88888
print(m)
print(n)
n[-1] = True
print(m)
print(n)