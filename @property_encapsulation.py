class person:
    def __init__(self):
        self.name=""
    @property
    def data(self):
        return self.name
    @data.setter
    def data(self,val):
        self.name=val
p1=person()
p1.data="vikram"
res=p1.data
print(res)
p1.data="vicky"
res1=p1.data
print(res1)

