k = int(input("Enter the number of digits: "))
i = 0
n = 0
while(k > 0):
    pages = 9*(10**i)
    digits = pages*(i+1)
    if(k - digits > 0):
        k -= digits
        n += pages
    else:
        n += k/(i+1)
        break
    i+=1
print(f"Number of pages is: {n}")