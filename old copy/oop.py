class student:
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age
        self.addr = "Viet Nam"
    def introduce(self):
        print(f"Ten: {self.name},tuoi:{self.age}, dia chi:{self.addr}")
# tao 1 bien tu student
a = student("Nguyen Van A",18)
print(f"Ten:{a.name}")
print(f"Dai Chi: {a.addr}")

a.introduce()