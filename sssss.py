A = ['9','8','7','6','5','4','3','0']
for i in range(len(A)):
    min_= i
    for j in range(i+1, len(A)):
        if A[min_] > A[j]:
            min_ = j
    A[i], A[min_] = A[min_], A[i]
for i in range(len(A)):
    print(A[i])
