#1st square:
#[0,0], [0,1], [0,2]
#       [1,1]
#[2,0], [2,1], [2,2]
#

#x = 0-3 (including 0-1-2-3)
#y=  0-3 (including 0-1-2-3)

def hourglassSum(arr):
    total = -83
    temp_total = 0
    for x in range(4):
        for y in range(4):
            temp_total = arr[x+0][y+0] + arr[x+0][y+1] + arr[x+0][y+2] + arr[x+1][y+1] + arr[x+2][y+0] + arr[x+2][y+1] + arr[x+2][y+2]
            if temp_total > total:
                total = temp_total

    return total


the_matrix = [
    [-9, -9, -9,  1, 1, 1],
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]
]
print(hourglassSum(the_matrix))
