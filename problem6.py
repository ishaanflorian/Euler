total = 0
for i in range (1, 101):
    square = i * i
    # print(square)
    total = square + total
print(total)

total2 = 0
for g in range(1, 101):
    total2 = total2 + g
square2 = total2 * total2
print(square2)

difference = square2 - total

print(difference)


    