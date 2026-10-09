#single-level inheritance
class A:
    def dip__A(self):
        print("inside A")
class B(A):
    def dip__B(self):
        print("inside B")
b1=B()
b1.dip__B()
b1.dip__A()

