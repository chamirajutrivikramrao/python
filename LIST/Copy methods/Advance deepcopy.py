#adv deep method
import copy
l1=[10,20,["nikky","kavya"],30]
print(l1)
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l1[2][0]="vicky"
print(l1)
print(l2)
l1[1]=200
print(l1)
print(l2)
