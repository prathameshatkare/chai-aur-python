num=int(input("Enter the number:"))


while(num>10 or num<0):
    print("oops!")
    b=int(input("Enter again:"))
    if b in range(0,10):
        print("Excellent")
        break