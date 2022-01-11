import numpy as np

a=np.ones((2,3))
b=np.full((3,2),2)

print(a)
print(b)


print(np.matmul(a,b))

c=np.identity(3)
print(np.linalg.det(c))

###########staistics

stats=np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats))
print(np.sum(stats))