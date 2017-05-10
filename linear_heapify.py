# Building hash in O(n) time and O(1) additional space. Inspired by https://www.youtube.com/watch?v=MiyLo8adrWw


def heapify(a):
    for i in range(len(a) // 2, -1, -1):
        parent = i

        while True:
            candidates = [parent, 2 * parent + 1, 2 * parent + 2]
            candidates = [e for e in candidates if e < len(a)]
            largest = max(candidates, key=lambda e: a[e])

            if largest == parent:
                break
            else:
                a[parent], a[largest], parent = a[largest], a[parent], largest

# Test
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
heapify(arr)
print(arr)
