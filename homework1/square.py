arr = input("Enter elements separated by spaces: ")
sum = 0
for i in arr.split():
    sum += int(i)**2
print("Sum of squares:", sum)
