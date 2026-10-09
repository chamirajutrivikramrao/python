#multi-level inheritance
class A:
    def dip__A(self):
        print("inside A")
class B(A):
    def dip__B(self):
        print("inside B")
class C(B):
    def dip__C(self):
        print("inside C")
c1=C()
c1.dip__C()
c1.dip__B()
c1.dip__B()
c1.dip__A()
