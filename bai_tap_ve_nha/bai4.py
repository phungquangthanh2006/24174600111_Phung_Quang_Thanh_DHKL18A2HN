print("hieu dien the: 220V")
print("cuong do dong dien: 2.7A")
t = int(input("nhap thoi gian su dung: "))
if t < 0:
    t = int(input("nhap lai thoi gian su dung: "))
else:
 Q = 220 * 2.7 * t 
 print(f"nhiet luong toa ra cua bong den là: {Q}(J)")
 so_dien = Q / 3600000
 print(f"so dien tieu thu cua bong den la: {so_dien}(kWh)")
 print("tien dien là 7000d/kWh")
 tien_dien = so_dien * 7000
 print(f"so tien dien can tra la: {tien_dien}")
