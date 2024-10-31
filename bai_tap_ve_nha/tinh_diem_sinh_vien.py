diem_chuyen_can = float(input("nhap diem chuyen can: "))
diem_giua_ki = float(input("nhap diem giua kì: "))
diem_cuoi_ki = float(input("nhap diem cuoi kì: "))
if diem_chuyen_can and diem_cuoi_ki and diem_giua_ki > 0:
   diem_trung_binh = (diem_chuyen_can + diem_cuoi_ki + diem_giua_ki) / 3
   if diem_trung_binh >= 9:
      print(f"diem trung binh la: {diem_trung_binh}")
      print("loai A")
   elif diem_trung_binh >= 7:
      print(f"diem trung binh cua ban la: {diem_trung_binh}")
      print("loai B")
   elif diem_trung_binh >= 5:
       print(f"diem trung binh cua ban la: {diem_trung_binh}")
       print("loai C")
   else:
       print(f"diem trung binh cua ban la: {diem_trung_binh}")
       print("loai D")
else:
   print("ban da nhap sai diem")
