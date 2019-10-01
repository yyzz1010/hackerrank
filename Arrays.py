import numpy

def arrays(arr):
    # complete this function
    # use numpy.array

    answer = numpy.array([arr], float)
    ans = numpy.flip(answer).flatten()
    return ans

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
