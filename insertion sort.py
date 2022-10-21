def insertionSort(n):
   for i in range(1, len(n)):
      key = n[i]
      j = i-1
      while j >=0 and key < n[j] :
         n[j+1] = n[j]
         j -= 1
      n[j+1] = key
n = [10,48,5,6,7,2,1,78,4,2]
insertionSort(n)
print ("The sorted array is:")
for i in range(len(n)):
   print (n[i])
