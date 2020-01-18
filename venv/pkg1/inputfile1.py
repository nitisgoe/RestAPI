try :
    size_input = int(input("Enter a number to calclute square: "))
    # square = int(size_input)**2
    print("The sqaure of number {}, is {}".format(size_input, size_input**2))
# print(f"Square of number {size_input} is {square}")4
except ValueError:
    print("Invalid Input")