a = float(input("nhap so thu nhat: "))
b = float(input("nhap so thu hai: "))
c = float(input("nhap so thu ba: "))
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c
print(f"so lon nhat trong 3 so {a}, {b}, {c} la: {so_lon_nhat}")