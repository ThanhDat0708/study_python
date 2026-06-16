import io_handle as io
import processing as pr
def main():
    dssv = io.ds_sv()
    diem_max = pr.sv_diem_max(dssv)
    diem_min = pr.sv_diem_min(dssv)
    print(f"sinh vien diem cao nhat danh sach: ")
    io.sinhvien(diem_max)
    print(f"sinh vien diem nho nhat danh sach: ")
    io.sinhvien(diem_min)
if __name__ == "__main__":
    main()