#duplicate strings
str=input("enter a str:")
str1=" "
for i in str:
    if i in str1:
        pass
    else:
        str1=str1+i
print(str1)

#space sentences
str=input("enter a sentence:")
print(str)
str1=str.lstrip()
print(str1)
str2=str.rstrip()
print(str2)
str3=str.strip()
print(str3)

#remove space of str
str=input("enter a  space str:")
str1=""
for i in str:
    if i in str1:
        pass
    else:
        str1=str1+i
print(str1)

#reverse a str
str=input("enter a str:")
rev=""
for i in str:
    rev=i+rev
print(rev)

#reverse a sentence
str=input("enter a sentence:")
str1=""
str2=str.split()
for i in str2:
    str1=i+" "+str1
print(str1)

#replace str in @
str=input("enter a to replace str:")
str1=" "
for i in str:
    if i=="a":
        str1=str1+"@"
    else:
        str1=str+i
print(str1)
        

