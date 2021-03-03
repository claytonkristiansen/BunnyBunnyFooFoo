array = [1, 4, 6, 3, 4, 5, 7, 4, 3, 23, 8, 5, 6, 3]

number = int(input("Give me thing: "))

i = 0

length = 14

found = False

while(i < length and (not found)):
    k = 0
    while(k < length):
        if(k != i):
            if(array[i] + array[k] == number):
                found = True
                print(f"yo yo yo my fool the two numbers are {array[i]} and {array[k]} and their indecis are {i} and {k} respectively")
                break
        k = k + 1
    i = i + 1
if(not found):
    print("none were found")

