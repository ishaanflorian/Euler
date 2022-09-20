
from multiprocessing.sharedctypes import Value


def is_Palindrome(x):
    x = str(x)
    z = x [::-1]
    if z == x:
        return True
    else:
        return False


plist = []
for i in range(100,1000):
    for j in range(100,1000):
        x = i * j
        is_pal = is_Palindrome(x)
        if is_pal == True:
            # print (i,j,x)
            plist.append(x)             



print(max(plist))

