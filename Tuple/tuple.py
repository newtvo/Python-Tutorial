# create tuple
tuple1 = ('hello', 1, 2.33, True)
print(type(tuple1))
print(tuple1)

# indexing
print(tuple1[0])

tuple2 = ('2nd', 4, 'ok')

# concatenate tuples
tuple3 = tuple1 + tuple2
print(tuple3)
print(len(tuple3))

# slicing
print(tuple3[0:3])

# sorting
tuple4 = (2, 3, 0, 9, 4, 6, 8)
print(sorted(tuple4))
tuple5 = sorted(tuple4)
print(type(tuple5))

# nested tuple
tuple6 = ('hello', 1, 2.3, ('2nd', True, 4), 'end')
print(tuple6[3])
print(tuple6[3][1])
