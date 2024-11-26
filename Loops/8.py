a=int(input("Enter the number:"))

if a==2 or a==3 :
    print("This is prime")
for i in range (2,a-1):
    if a%i ==0:
        print("Not Prime!")
        break
    
    print("This is Prime") 
    break