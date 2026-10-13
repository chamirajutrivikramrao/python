class animal:
    def eat(self):
        print("animal can eat")
    def walk(self):
        print("animal can walk")
class dog(animal):
    def sound(self):
        print("dog is barking")
class tiger(animal):
    def sound(self):
        print("tiger is roaring")
d1=dog()
t1=tiger()
def allow(t):
    t.eat()
    t.walk()
    t.sound()
allow(d1)
allow(t1)
