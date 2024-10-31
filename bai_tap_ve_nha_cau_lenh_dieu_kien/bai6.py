print("chao mung ban den voi rap chieu phim ABC")
print("xin moi ban lua chon the loai phim ban muon xem")
print("1. phim tinh cam")
print("2. phim kinh di")
print("3. phim hoat hinh")
print("4. phim khoa hoc vien tuong")
lua_chon_cua_ban = input("hay nhap lua chon cua ban: ")
if lua_chon_cua_ban == "1":
    print(f"ban da chon phim tinh cam, chuc ban xem phim vui ve")
elif lua_chon_cua_ban == "2":
    print(f"ban da chon phim kinh di, chuc ban xem phim vui ve")
elif lua_chon_cua_ban == "3":
    print(f"ban da chon phim hoat hinh, chuc ban xem phim vui ve")
elif lua_chon_cua_ban == "4": 
    print(f"ban da chon phim khoa hoc vien tuong, chuc ban xem phim vui ve")
else:
    print("ban da nhap sai, xin vui long nhap lai")

