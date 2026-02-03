def utils(a, l, m, r):
    aL = []
    aR = [] 
    nL, nR = m - l + 1, r - m
    
    for i in range(nL):
        aL.append(a[l + i])
    for j in range(nR):
        aR.append(a[m + 1 + j]) 
        
    i, j, k = 0, 0, l   
    while i < nL and j < nR:
        if aL[i] <= aR[j]:
            a[k] = aL[i]
            i += 1
        else:
            a[k] = aR[j]
            j += 1
        k += 1
        
    while i < nL:
        a[k] = aL[i]
        i += 1
        k += 1
    while j < nR:
        a[k] = aR[j]
        j += 1
        k += 1

def mergeSort(a, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(a, l, mid)
        mergeSort(a, mid + 1, r)
        utils(a, l, mid, r)