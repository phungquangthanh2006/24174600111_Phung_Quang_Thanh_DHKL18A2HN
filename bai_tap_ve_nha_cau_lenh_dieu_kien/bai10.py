tien_luong = float(input("nhap tien luong cua nhan vien: "))
if tien_luong > 0:
    if tien_luong >= 15:
        tien_thue = tien_luong * 0.3
        luong_rong = tien_luong - tien_thue
    elif tien_luong > 7 and tien_luong < 15:
        tien_thue = tien_luong * 0.2
        luong_rong = tien_luong - tien_thue
    else:
        tien_thue = tien_luong * 0.1
        luong_rong = tien_luong - tien_thue
    print(f"thue thu nhap cua ban la: {tien_thue }trieu")
    print(f"so tien ban nhan duoc con lai la: {luong_rong} trieu")
else:
    print("ban da nhap sai so tien, vui lòng nhap lai")

