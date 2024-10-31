so_nam = int(input("nhap so nam: "))
if so_nam > 0:
    if so_nam % 4 == 0 and (so_nam % 100 != 0 or so_nam % 400 != 0):
      print("day la nam nhuan")
    else:
       print("day khong phai nam nhuan")
else:
   print("ban da nhap sai so nam")


