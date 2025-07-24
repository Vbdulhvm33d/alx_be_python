#user input for shape size
size = int(input("Enter the size of the pattern: "))
#initializing the row size
row = 0
while row < size:
    #here, I learned that integers are non-iterable and that the only way you can iterate through a single int is to declare
    #it as I did below.
    for int in range(size):
        print("*", end=" ")
    print()
    row += 1