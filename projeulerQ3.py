import math

x = 600851475143

def isPrime(a):
    if a == 2:
        return True
    i=2
    while (i <= math.sqrt(a)):
        if a%i == 0:
            return False
        i+=1
    return True

list_prime = []
i=math.floor(math.sqrt(x))
while (i>math.sqrt(i)):
    if (isPrime(i) == True) and (x%i) == 0:
        print (i)
        break
    i-=1
