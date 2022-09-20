
import time
from math import remainder

start_time = time.time()

nums = []

for i in range(1, 21):
    nums.append(i)

print (nums)
numerator = 1
found = False
while (found == False):
    x = 0
    for den in nums:
         remainder = numerator % den
        #  print (numerator, den, remainder)
         x = x + remainder
    # print (x)
    if x == 0:
        found = True
        print (numerator)
    numerator = numerator + 1

end_time = time.time()
total_time = end_time - start_time
print(total_time)

