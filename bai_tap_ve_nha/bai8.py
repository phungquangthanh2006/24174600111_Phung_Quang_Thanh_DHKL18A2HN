x = float(input("nhap vao x: "))
if x < 0 and x == 1:
   x = float(input("nhap lai x: ")) 
else:
 import math
 gia_tri_bieu_thuc  = math.log(x,4) + math.log(2,x)
 print(f"gia tri bieu thuc f(x) la: {gia_tri_bieu_thuc:.2f}")