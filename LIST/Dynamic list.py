l=[]
i=0
while True:
    num=int(input("enter a num:"))
    l.insert(i,num)
    i=i+1
    print("do you want to continue")
    print("press 1.YES 2.NO")
    choice=int(input())
    if choice==1:
        continue
    else:
        break
print(l)
