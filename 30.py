def computePower(n):
    """
    Returns integer: the 4th power of n
    """
    return n*n*n*n*n

i = 1
sumAns = 0
limit = 10000000

while (i<limit):
    sumDigits = 0
    ilist = map(int, str(i))
    for digit in ilist:
        sumDigits += computePower(digit)
#    print i, sumDigits
    if sumDigits == i:
        sumAns += i
        print (i)
    i+=1
        
print (sumAns)
