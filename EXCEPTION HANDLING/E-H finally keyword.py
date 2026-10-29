def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error ocurred in fun1")
    print("leaving fun1")
def fun2():
    print("entering fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error ocurred in fun2")
        raise e
    finally:
         print("leaving fun2")
print("program started")
fun1()
print("program ended")
