#1 1 2 3 5 8 13 21 34 


arr = [1, 1]

startingNumber = int(input("First: "))
endingNumber = int(input("Last: "))

i = 2
num = arr[i - 1] + arr[i - 2]
while num <= endingNumber:
    arr.append(num)
    i = i + 1
    num = arr[i - 1] + arr[i - 2]

index = 0
while(arr[index] < startingNumber):
    index = index + 1

between = len(arr) - index

print(between)
print(arr[index:])

#3 13

#1 1 2 3 5 8 13