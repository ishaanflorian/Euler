# Door Code Recognizer
# Our apartment building will let you enter if you press in four-digit sequence. Once you enter the numbers incorrect 5 times, permanently block access.


password = 1234
print (type(password))
access = False

while (access == False):
    n = input("Enter the door code ")

    code = int(n) 

    print (n)

    print (type(n))

    if code == password:
        access = True
        print ("Access granted")
    else:
        print ("Access Denied")
        


