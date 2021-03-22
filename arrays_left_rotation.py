def rotLeft(a, d):
  l1 = a[0:d]
  l2 = a[d::]
  return l2 + l1


print(rotLeft([1, 2, 3, 4, 5], 2))


def arrRot(arr, num):
  el = 0
  for i in range(num):
    el = arr.pop(0)
    arr.append(el)
  return arr

print(arrRot([1,2,3,4,5], 2))
