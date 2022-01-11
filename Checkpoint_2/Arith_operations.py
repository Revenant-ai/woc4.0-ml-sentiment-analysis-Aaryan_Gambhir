import numpy as np

arr=np.array([1,2,3,4],dtype="float16")

print("Addition")
print(arr+2)

print("Subtraction")
print(arr-2)

print("Multiplication")
print(arr*4)

print("Division")
print(arr/2)

print("Addition of two arrays")
b=np.array([10,20,30,40])
print(arr+b)
      
print("power of a number")
print(arr ** 3)

print("trgio values of an array")
print(np.cos(arr))

