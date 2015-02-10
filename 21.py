def findDivSum(n):
    """
    Return sum of proper divisors of n
    """
    i = 1
    sum = 0
    while i <= n/2:
        if n%i == 0:
            sum += i 
        i+=1
    return sum

i=2
sumAmi = 0
amiList = []
while i<10000:
    sum1 = findDivSum(i)
    sum2 = findDivSum(sum1)
    if (i == sum2) and  (i != sum1) and i not in amiList:
        sumAmi += i + sum1
        amiList.append(i)
        amiList.append(sum1)
        print("Ami 1: "+ str(i) +"\t Ami 2: "+ str(sum1))
    i+=1

print (sumAmi)

