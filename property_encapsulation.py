
class person:
    def __init__(self):
        self.name=""
    def getter(self):
        return self.name
    def setter(self,val):
        self.name=val
    getset=property(getter,setter)
p1=person()
p1.getset="vikram"
res=p1.getset
print(res)
p1.getset="vicky"
res1=p1.getset
print(res1)
