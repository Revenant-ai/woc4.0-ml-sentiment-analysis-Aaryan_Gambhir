import numpy as np

a=np.array([1,2,3],dtype='int16')
print(a)

b=np.array([[9,1,2],[4,5,6]])
print(b)

#It returns the dimension of the array formed using numpy library
print(a.ndim)
print(b.ndim)

print(a.shape)#returns a vector i.e the number of rows and col so in 1D array the number of elements will be returned

print(b.shape)#Here it will return (2,3)as it is a 2d array and we can map the nuber of rows and cols, hence 


#Get Type of the array
print(a.dtype)
print(b.dtype)

#Get Size
print(a.itemsize)
print(b.itemsize)

#total size i.e the size of the elements
print(a.size)

#get total memory occupied by the list
print(a.nbytes)