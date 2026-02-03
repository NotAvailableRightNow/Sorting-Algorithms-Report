def utils(arr, n, rt):
    while True:
        mx = rt
        l = 2 * rt + 1
        r = 2 * rt + 2

        if l < n and arr[l] > arr[mx]:
            mx = l
        if r < n and arr[r] > arr[mx]:
            mx = r

        if mx != rt:
            arr[rt], arr[mx] = arr[mx], arr[rt]
            rt = mx 
        else:
            break
        
def heapSort(a):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        utils(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i] 
        utils(a, i, 0)