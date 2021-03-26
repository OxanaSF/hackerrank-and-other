def makeAnagram(a, b):
  word1 = {}
  word2 = {}
  deleted = 0

  for i in a:
    if i in word1:
      word1[i] += 1
    else:
      word1[i] = 1

  for i in b:
    if i in word2:
      word2[i] += 1
    else:
      word2[i] = 1

  for letter, count in word1.items():

    if letter not in word2:
      deleted += count
    else:
      if count > word2[letter]:
        deleted += count - word2[letter]
      elif word2[letter] > count:
        deleted += word2[letter] - count

  for letter, count in word2.items():
    if letter not in word1:
      deleted += count

  return deleted


# print(makeAnagram('cde', 'abc'))
print(makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'))
