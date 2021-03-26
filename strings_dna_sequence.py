# input: "aaaabbсaa"
# expected output: "a4b2с1a2"

#second solution. The latest
s = 'aaaabbcaa'
s = s + '  '
dna = ''
count = 0
for i in range(len(s)-1):
  count += 1
  if s[i] != s[i+1]:
    dna += s[i]
    dna += str(count)
    count = 0

print(dna)

print('********************')

#First solution
s = 'aaaabbcaa'
count = 1
arr_letters = []
arr_nums = []
i = 0
dna = ''

while i < len(s):
  if arr_letters and arr_letters is not None and arr_letters[-1] == s[i]:
    count += 1
    arr_letters.pop()
  else:
    count = 1

  arr_letters.append(s[i])

  if arr_nums and arr_nums is not None and arr_nums[-1] < count:
    arr_nums.pop()
    arr_nums.append(count)
  else:
    arr_nums.append(count)

  i += 1

for i, j in zip(arr_letters, arr_nums):
  dna += str(i)
  dna += str(j)

print(dna)
