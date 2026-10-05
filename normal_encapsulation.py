class person:
    def __init__(self):
        self.name=""
    def getter(self):
        return self.name
    def setter(self,val):
        self.name=val
p1=person()
p1.setter("vikram")
res=p1.getter()
print(res)
p1.setter("vicky")
res1=p1.getter()
print(res1)
