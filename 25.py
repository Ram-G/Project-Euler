a = 0
b = 1
c = 1

count = 2

while (len(str(a)) < 1000):
    a = b+c
    c = b
    b = a
    count+=1
print (a, count)
