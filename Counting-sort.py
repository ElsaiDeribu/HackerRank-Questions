def countsort(n, arr):
    count = []
    for i in range(102):
        count.append(0)
    for j in range(n):
        count[arr[j]] += 1

    return count
