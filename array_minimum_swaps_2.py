#explaination:
#indexes: 0 1 2 3 4 5 6
#numbers:[1,2,3,4,5,6,7]
#conclusion: in an ordered array(list) of consecutive integers  beginning with 1
#[1, 2, 3, ..., n] without any duplicates
# the integer is always equel to its index + 1
#or to check the correct order the index should be #equel to the integer - 1

def minimumSwaps(arr):
    swap = 0
    for i in range(len(arr)):
        while arr[i]-1 != i:
            num = arr[i]
            arr[num-1], arr[i] = arr[i], arr[num-1]
            swap += 1
    return swap


arr_test = [1, 3, 5, 2, 4, 6, 7]
print(minimumSwaps(arr_test))

