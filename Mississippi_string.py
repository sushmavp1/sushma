import operator
str1 = "mississippi"

freq = {}

for i in str1:
  if i in freq:
     freq[i] += 1
  else:
    freq[i] = 1

 a = sorted(freq,key=operator.itemgetattr(1),reverse=True)

print("Count of all characters is :\n" + str(freq))
print('sorted list(in descending):",a')
