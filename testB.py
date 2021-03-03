

length = int(input("Enter length: "))

array = []
i = 0

while(i < length):
    element = int(input(f"Enter element at index {i}: "))
    if(element > 0):
        array.append(element)
        i = i + 1
    else:
        print("You idiot, I said greater than 0!!!!!!!!!!!!!!")
    
print(array)