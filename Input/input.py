print('Please write your input: ')
s = input()
print('Your input: ', s)

print('*'* 30)

x = int(input('Please write something: '))
print('Your result: ', x)
print(type(x))
print('*'* 30)

def StrToBool(s):
    return s.lower() in ("true", "t", "1", "yes")

y = input('Please choose TRUE/FALSE: ')
print(StrToBool(y))