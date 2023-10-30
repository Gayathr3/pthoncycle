n = int(input("enter the number of values"))
a = []
for i in range(0,n):
    c = int(input("enter the value"))
    if c > 100:
     a.append("over")
    else:
        a.append(c)
    print(a)