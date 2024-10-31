S = float(input("nhap quang duong: "))
if S > 0:
    print("nhap xe ban muon di")
    print("1. xe 4 cho")
    print("2. xe 7 cho")
    chon_xe = input("loai xe ban muon di la: ")
    thoi_gian_cho = float(input("nhap thoi gian cho: "))
    if thoi_gian_cho > 5:
       tien_cho_xe = (thoi_gian_cho - 5) * 800
    else: 
       tien_cho_xe = 0
    if chon_xe == "1":
       print(f"ban da lua chon xe 4 cho")
       if S < 0.8:
           so_tien = 11000 + tien_cho_xe
           print(f"so tien ban phai tra la: {so_tien}d")
       elif S > 0.8 and S < 20:
           so_tien = 11000 + (S - 0.8) * 12100 + tien_cho_xe
           print(f"so tien can phai tra la: {so_tien}d ")
       else:
           so_tien = 11000 + (20 * 12100 ) + ((S - 20.8)*10000) + tien_cho_xe
           print(f"so tien ban can phai tra là: {so_tien}")
    elif chon_xe == "2":
        print("ban da lua chon xe 7 cho")
        if S < 0.8:
            so_tien = 13000 + tien_cho_xe
            print(f"so tien ban phai tra la: {so_tien}d")
        elif S > 0.8 and S < 30:  
            so_tien = 13000 + (S - 0.8) + tien_cho_xe
            print(f"so tien ban phai tra la: {so_tien}d")
        else:
            so_tien = 13000 + (30 * 14100) + (S - 30.8)*12000 + tien_cho_xe
            print(f"so tien ban phai tra la: {so_tien}d")
    else:
        print("ban da chon sai loai xe")
else:
    print("ban da nhap sai quang duong ban muon di")

