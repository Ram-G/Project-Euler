list = []

a = 2
power = 1

while (a <= 100):
    b = 2
    while (b <= 100):
        power = pow(a,b)
        if power not in list:
            list.append(power)
        b+=1
    a+=1


        
        
