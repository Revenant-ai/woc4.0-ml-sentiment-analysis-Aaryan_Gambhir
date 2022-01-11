import numpy as np

print("\n Accessing/Changing specific elements,ows,columns \n")

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print("\n")

print("get specific element use [row,column] of the desired element")
print(a[1,5])

print("get specific element row")
print(a[1,:])

print("get specific element col")
print(a[:,1])

print("getting fancy stuff [startindex:endindex:stepsize]")
print(a[0,1:6:2])

print("change value of a particular element")
a[1,5]=20
print(a)


print("changing a column")
a[:,2] = [3,4]
print(a)


print("3d example")
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

print("get specific element work outside in")
print(b[:,:,1])