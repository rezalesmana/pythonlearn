for i in range(1,20):
    print("i is now {}".format(i))

number = "8,231,319,176,452"
for i in range(0, len(number)):
    print(number[i])

number = "8,231,319,176,452"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])

cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)

print("The number is {}".format(newNumber))