n = 5

print("Output A: ")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for k in range(1, i + 1):
        print(k, end="")
    
    print()


print("\nOutput B: ")
m = 7
a = 1

while a <= m:
    c = 1
    while c <= a:
        print(a, end="")
        c += 1
        
    print()
    
    if a == 5:
        a = 6
    elif a ==6:
        a = 7
    else:
        a += 2