s = "Hello Mi AI"
print(s[6:11])

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(d[-3:])

for i in d:
    print("Gía trị i = ", i)

for y in s:
    print("Gía trị y = ", y)

for i in range(1, 10):
    if i == 5:
        break
    if i == 2:
        print("số 2 sẽ bị mất")
        continue
    print(i)

i = 0
while i < 10:
    print(i)
    i = i + 1

import random

a = random.random()
print(a)


def caculate_ABC(a, b):
    return a * b

x = 3
y = 2
z = caculate_ABC(x, y)
print(z)