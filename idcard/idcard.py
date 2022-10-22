from tokenize import Name
import code128;

# input

name = input('what is your name? ')
section = input('what is your section? ')
isValidBarcodeNum = False

while isValidBarcodeNum == False:
    barcode_num = input('what is your barcode number? ')
    # verification
    try:
        input_type = int(barcode_num)
        isValidBarcodeNum = True
    except ValueError:
        isValidBarcodeNum = False 
        
    if isValidBarcodeNum:
        #print(input_type)
        print("Valid Number")
    else:
        print("Invalid Number")





# Prints
print(name)
print(section)
print(barcode_num)

if isValidBarcodeNum:
    #print(input_type)
    print("Valid Number")
else:
    print("Invalid Number")



# code128.image(barcode_num).save(Name)  # with PIL present

with open("barcode-" + name + ".svg", "w") as f:
        f.write(code128.svg(barcode_num))