#shallow copy
a=[10,20,["romantic","guy"],30]
print(a)
b=a
print(a)
print(b)
a[1]=200
a[2][1]="girls"
print(a)
print(b)
