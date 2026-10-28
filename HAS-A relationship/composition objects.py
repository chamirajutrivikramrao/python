class os:
    def __init__(self):
        self.status=True
        print("os is ready")
        print("os is installing")
class mobile:
    def __init__(self,name):
        self.mname=name
        self.o=os()
        print("os is installed")
m1=mobile("realme")
print(m1.mname)
print(m1.o.status)
del m1
print(m1.o.status)
