
def is_prime(number):
    flag = False
    for i in range (2, number - 1):
      remainder = number % i
      if remainder == 0:
        flag = True
        break

    if flag == False:
        return True
    else:
        return False
    

x = 600851475143

factors = []
for i in range(1, x+1):
    y = x % i
    if y == 0:
        isPrime = is_prime(i)
        if isPrime == True:
            factors.append(i)

    # print(x)
    # print(i)
    # print (y)
    # print (" ")
print(factors)