# viet chuong trinh in ra cac so nguyen to tu 1 den n
import math
def check_snt(n: int ) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if  n % i == 0:
            return False
        
    return True 
#end function
def main():
    n = int(input("Nhap vao 1 so: "))
    print(f"so nguyen to tu 1 den {n} la:")
    for i in range(1, n + 1):
        if check_snt(i) == True:
            print(f"{i} ", end="")

if __name__ == "__main__":
    main()