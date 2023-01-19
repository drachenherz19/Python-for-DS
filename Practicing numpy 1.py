import numpy as np
#1 Dimensional Array:
a = np.array([1,2,3])
print(a)
#2 Dimensional Array:
b = np.array([[1,2,3],[4,5,6]])
print(b)
#3x4 array of zeroes:
c = np.zeros((3,4))
print(c)
#Arrange numbers between lower (1) and upper limit (10) with an interval of 3:
d = np.arange(1,10,3)
print(d)
#Printing even numbers between 10 and 20:
x = np.arange(10,20,2)
print(x)
#Arrange 'x' numbers with equal spacing between lower (1) and upper (20) limit:
y = np.linspace(1,20,4)
print(y)
#Have an array of the same value:
z = np.full((2,3),6)
print(z)
#Fill array of any size with random values:
o = np.random.random((10, 12))
print(o)