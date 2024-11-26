import math

def answer(radius):
    pi=math.pi
    area=pi*(radius**2)
    area=round(area,3)
    circumference=2*pi*radius
    circumference=round(circumference,3)
    print("Area of circle is:",area)
    print("Circumference of circle is:",circumference)
radius=int(input("Enter kar:"))
print(answer(radius))