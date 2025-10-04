n = int(input())
print("is it daytime?")
time = bool(input())
if n >= 100:
    print("price =", n*0.06)
elif n >= 20:
    print("price =", n*0.09)
elif time == True:
    print("price =", n*0.79+0.7)
else:
    print("price =", n*0.9+0.7)