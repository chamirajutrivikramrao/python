#decorators()
def main():
    str=input("enter a str:")
    return str
def outer(ptr):
    print("inside outer")
    def inner():
        print("inside inner")
        res=ptr()
        ans=res.upper()
        print(ans)
        print("leaving inner")
    return inner
ref=outer(main)
ref()
