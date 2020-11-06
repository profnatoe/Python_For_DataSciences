import numpy as np


# np.array((1,0,0),(0,1,0),(0,0,1,dtype=float) does not create a 2-D Array
#Because the array was not declared properly for one.
#a simple array is declared like this np.array([(0,0,0)]) of which [] was omitted from the above given statement

np.array([(1, 0, 0), (0, 1, 0), (0,0,1)])


#

#The Difference between

a = np.array([0, 0,0])

#and

a = np.array([[0,0,0]])


# is that the first array has 1 axe and the shape of the array is (3,) 
# while the second array has 2 axes or dimensions and the shape of the array is (1, 3) => 1 row and 3 columns


#3 by 4 by 4

arr = np.linspace(1, 48, 48).reshape(3,4,4)


print(arr[1,0,-1])
print(arr[0:1,2])
print(arr[2].flatten())
print(arr[:,1,:2].flatten())
print(arr[2,:,:1:-1].flatten())
print(arr[:,::-1,0].flatten())
print(arr.reshape(12,4)[::11,::3].flatten())
print(arr.reshape(3,2,2,4)[[1,2],[1,0],:].reshape(4,4).flatten())


