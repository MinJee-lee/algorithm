target = [9, 8, 7 , 6, 5, 4, 3, 2, 1]

def merge_sort(array):
    # global target 
    if len(array) == 1:
        return array
    half = int(len(array)/2)
    a = merge_sort(array[0:half])
    b = merge_sort(array[half: len(array)])
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    while len(a) > 0:
        c.append(a.pop(0))
    while len(b) > 0:
        c.append(b.pop(0))
    print(c)
    return c
        
        
print(merge_sort(target))