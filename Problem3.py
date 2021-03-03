digitString = input("Enter string input: ")

good = False

while(not good):
    if(digitString[0] == '0' or digitString[-1] == '0'):
        print("bad boy enter no zeros at beginning or end")
        digitString = input("Enter string input: ")
    else:
        good = True

strArray = digitString.split(' ')
intArray = []

for x in strArray:
    intArray.append(int(x))

intReverseArray = []

for x in intArray:
    intReverseArray.insert(0, x)

num1 = 0
num2 = 0

sig = len(intArray) - 1

for x in intArray:
    num1 += x * 10**sig
    sig = sig - 1

sig = len(intReverseArray) - 1

for x in intReverseArray:
    num2 += x * 10**sig
    sig = sig - 1

sum = num1 + num2

addArray = []

while(sum > 0):
    addArray.insert(0, sum % 10)
    sum = int(sum / 10)

print(addArray)




#1000
# 300
#  20
#   8
#1328