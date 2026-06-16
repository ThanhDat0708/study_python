# Nhập xuất thông tin 
def  thongtin_sv():
    ten = input("Nhap ten sinh vien:")
    lop = input("Nhap lop:")
    diem = float(input("Nhap diem:"))
    return {"ten sinh vien":ten,"lop":lop,"diem":diem}
def ds_sv():
    n = int(input("Nhap so luong sinh vien"))
    list_sv = []
    for i in  range(n):
        print(f"Nhap thong tin sinh vien thu {i+1}:")
        sv = thongtin_sv()
        list_sv.append(sv)
    return list_sv
def sinhvien(sv):
    print(f"Tên:{sv['ten sinh vien']},Lớp:{sv['lop']},Điểm:{sv['diem']}")