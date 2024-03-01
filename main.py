from numpy import int32, int64, ndarray, array, random

np_arrayA: ndarray[int32] = array(random.randint(0, 101, size=10))
print(np_arrayA)

np_arrayB: ndarray[int32] = array(random.randint(0, 2, size=(5,5)))
print(np_arrayB, np_arrayB.max(), np_arrayB.mean(), np_arrayB.min())

np_arrayC: ndarray[int32] = array(random.randint(0, 2, size=10))
np_arrayD: ndarray[int64] = array([int64(i * 10) for i in np_arrayC])
print(np_arrayD)

np_arrayE: ndarray[int32] = array(random.randint(0, 10, size=(3,3)))
np_arrayE[1, 0::] = -1
print(np_arrayE)

