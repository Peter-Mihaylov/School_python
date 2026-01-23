arr = input()
total = 0
for word in arr.split():
    total += len(word)
print("Average length of words:", total / len(arr.split()))