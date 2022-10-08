#List
l1=['Hello','Shivam',10,20,'Name',40]
print(l1)
print(type(l1))

#Access item of a list
l1=[10,20,30,40,50,60,70,80]
print(l1[-4])
print(l1[3:5])
print(:5)
print(6:)

#Change the list item
l1=[10,20,30,40,50]
l1[0]="Shivam"
l1[3]=46
print(l1)
l1[1:3]=['Shivam','Singh']
print(l1)
l1=[1:2]=['Shivam','Singh']
print(l1)

#Insert()
l1=[10,20,30,40]
l1.insert(2,25)
print(l1)

#Append()
l1=[10,20,30,40]
l1.append(50)
print(l1)

#Extend()
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l1.extend(l2)
print(l1)
tuple=(6,7,8,9)
l1.extend(tuple)
print(l1)

#Remove()
l1=[10,20,30,40]
l1.remove(20)
print(l1)

#Pop()
l1=[10,20,30,40]
l1.pop(20)
print(l1)

#Del()
l1=[10,20,30,40]
del l1[0]
print(l1)
del l1
print(l1)
