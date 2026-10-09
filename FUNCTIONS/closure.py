#closure()
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
        print("leaving inner")
    return inner
ref=outer()
ref()
