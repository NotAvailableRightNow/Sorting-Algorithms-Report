import numpy as np

def gen(n, p, lim):
    dl = []

    a = np.random.uniform(-lim, lim, p)
    a.sort()
    dl.append(a)

    a = np.random.uniform(-lim, lim, p)
    a = np.sort(a)[::-1]
    dl.append(a)

    for _ in range(3):
        a = np.random.uniform(-lim, lim, p)
        dl.append(a)

    for _ in range(5):
        a = np.random.randint(-int(lim), int(lim), p)
        dl.append(a)
        
    return dl
    
    