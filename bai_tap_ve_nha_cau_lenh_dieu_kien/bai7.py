print("nhap phuong trinh 1: ")
a1 = float(input("nhap a1: "))
b1 = float(input("nhap b1: "))
c1 = float(input("nhap c1: "))
print("nhap phuong trinh 2:")
a2 = float(input("nhap a2: "))
b2 = float(input("nhap b2: "))
c2 = float(input("nhap c2: "))
if a1/a2 == b1/b2:
    if a1/a2 == b1/b2 != c1/c2:
       print("he phuong trinh tren vo nghiem")
    elif a1/a1 == b1/b2 == c1/c2:
       print("he phuong trinh vo so nghiem")
else:
    x = (b1*c2 - b2*c1) / (a2*b1 - b2*a1)
    print(f"he phuong trinh tren co nghiem x= {x}")
    y = (c1 - a1*x) / b1
    print(f"he phuong trinh tren co nghiem y= {y}")

