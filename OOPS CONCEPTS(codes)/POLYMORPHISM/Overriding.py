class A:
    def disp(self):
        print("inside a")
class B(A):
    def disp(self):
        print("inside b")
class C(B):
    def disp(self):
        print("inside c")
c1=C()
c1.disp()
c1.disp()
c1.disp()


