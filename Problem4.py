strInput = input("gimme that input: ")

length = len(strInput)

print(f"Length of the string {strInput} is {length}")

if(length % 2 == 0):
    index = 0
    while(index < length):
        print(strInput[index], end='\t')
        index += 2
    print()
    index = 0
    while(index < length):
        print(index, end='\t')
        index += 2
else:
    index = 1
    while(index < length):
        print(strInput[index], end='\t')
        index += 2
    print()
    index = 1
    while(index < length):
        print(index, end='\t')
        index += 2

