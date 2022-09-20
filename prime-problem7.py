

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
    


primes = []
for i in range (1,1000000):
    # print(i)
    x = is_prime(i)
    if x == True:
        primes.append(i)

# print(primes)
print(primes[10001])
    



