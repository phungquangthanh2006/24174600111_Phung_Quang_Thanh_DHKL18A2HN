print("nhap diem M")
x = float(input("nhap x: "))
y = float(input("nhap y: "))
print("nhap tam I")
a = float(input("nhap a: "))
b = float(input("nhap b: "))
R = float(input("nhap ban kinh R: "))
if R > 0:
    do_dai_IM = (((a-x)**2) + ((b-y)**2)) ** (1/2)
    print(f"do dai IM la: {do_dai_IM}")
    if do_dai_IM > R:
        print(False)
    else:
        print(True)
else:
    print("ban da nhap sai ban kinh R")
    