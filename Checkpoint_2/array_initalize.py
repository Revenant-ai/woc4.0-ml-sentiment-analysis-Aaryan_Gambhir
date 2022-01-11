import numpy as np

print("All 0's matrix ")
arr=np.zeros((2,3))
print(arr)

print("All 1's matrix")
arr=np.ones((2,3),dtype='int32')
print(arr)

print("Any other number")
arr=np.full((2,2),99,dtype='float32')
print(arr)

print("Any other number full like")
arr_new=np.full_like(arr,4)
print(arr_new)

print("Random matrix decimal number")
arr=np.random.rand(4,2)
print(arr)

print("Random matrix Integer number")
arr=np.random.randint(4,8,size=(3,3))
print(arr)

print("Identity matrix")
arr=np.identity(4)
print(arr)

print("Repeat an array")
arr=np.array([[2,4,6 ]])
r1=np.repeat(arr,3,axis=0)
print(r1)


print("____EXERCISE______")
answer=np.ones((5,5),dtype='int16')
answer[1:-1,1:-1]=0
answer[2][2]=9
print(answer)