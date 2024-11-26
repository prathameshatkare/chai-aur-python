n=int(input("Enter the number:"))
for i in range(1,11):
    if i==5:
        continue
    a=i*n
    print(n,"*",i,"=",a)
