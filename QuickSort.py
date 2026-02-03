import random

def utils(a, l, r):
    p = a[random.randint(l, r)]
    i = l - 1
    
    for j in range(l, r):
        if a[j] <= p:
            i += 1
            a[i], a[j] = a[j], a[i]
            
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

def quickSort(a, l, r):
    if l < r:
        p = utils(a, l, r)
        quickSort(a, l, p - 1)
        quickSort(a, p + 1, r)
