class A:
    def disp(self,a,b,c):
        print(a)
        print(b)
        print(c)
class B(A):
    def disp(self,a,b):
        print(a)
        print(b)
class C(B):
    def disp(self,a):
        print(a)
c1=C()
c1.disp(10)
c1.disp(10,20)
c1.disp(10,20,30)
