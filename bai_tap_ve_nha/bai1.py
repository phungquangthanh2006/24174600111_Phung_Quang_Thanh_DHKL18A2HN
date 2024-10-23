r = float(input("nhap ban kinh: "))
if r < 0:
    print("loi phuong trinh vi ban kinh luon lon hon 0")
h = float(input("nhap chieu cao: "))
if h < 0:
    print("loi phuong trinh vi chieu cao luon lon hon 0")
else:      
 dien_tich_xung_quanh = 2 * 3.14 * r * h
 print(f"dien tich xung quanh cua hinh tru la: {dien_tich_xung_quanh:.2f} ")
 dien_tich_toan_phan = 2 * 3.14 * r * ( r + h )
 print(f"dien tich toan phan cua hinh tru la: {dien_tich_toan_phan:.2f}")
 the_tich = 3.14 * (r*r) * h
 print(f"the tich hinh tru la: {the_tich:.2f}")