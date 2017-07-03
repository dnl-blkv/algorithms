a = [1, 3, 8, 12, 15]
b = [4, 12, 17, 0, 0, 0, 0, 0]

i = len(a) - 1
j = len(b) - len(a) - 1
k = len(b) - 1

while i >= 0:
    if j >= 0:
        if a[i] > b[j]:
            while i >= 0 and a[i] >= b[j]:
                b[k] = a[i]
                i -= 1
                k -= 1
        else:
            while j >= 0 and a[i] < b[j]:
                b[k] = b[j]
                j -= 1
                k -= 1
    else:
        while i >= 0:
            b[k] = a[i]
            i -= 1
            k -= 1

print(b)
