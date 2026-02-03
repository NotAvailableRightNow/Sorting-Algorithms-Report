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
        
        
# def quickSort(a, l, r):
#     if l >= r:
#         return
#     m = (l + r) // 2
#     a[m], a[r] = a[r], a[m]
#     p = a[r]
#     i = l - 1
    
#     for j in range(l, r):
#         if a[j] < p:
#             i += 1
#             a[i], a[j] = a[j], a[i]
            
#     a[i + 1], a[r] = a[r], a[i + 1]
    
#     quickSort(a, l, i)
#     quickSort(a, i + 2, r)

# def quickSort(a):
#     if len(a) <= 1:
#         return a
#     else:
#         pivot = a[0]
#         less = [i for i in a[1:] if i <= pivot]
#         greater = [i for i in a[1:] if i > pivot]
#         return quickSort(less) + [pivot] + quickSort(greater)
