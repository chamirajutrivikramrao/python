def main():
    print("inside main")
    yield 1
    print("inside yield 1")
    yield 2
    print("inside yield 2")
    yield 3
    print("inside yield 3")
res=main()
print(res)#address object generator
print(next(res))#1
print(next(res))#2
print(next(res))#3
print(next(res))#stop iteration  error





