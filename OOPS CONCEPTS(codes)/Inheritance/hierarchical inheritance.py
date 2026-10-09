

#hierachical inheritance
class A:
    def dip__A(self):
        print("inside A")
class B(A):
    def dip__B(self):
        print("inside B")
class C(A):
    def dip__C(self):
        print("inside C")
b1=B()
c1=C()
b1.dip__B()
b1.dip__A()
c1.dip__C()
c1.dip__A()

