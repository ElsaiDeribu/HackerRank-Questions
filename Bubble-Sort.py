def countSwaps(a):
    counter = 0
    indexing_length = len(a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if a[i] > a[i + 1]:
                sorted = False
                a[i], a[i + 1] = a[i + 1], a[i]
                counter += 1
    print("Array is sorted in " + str(counter) + " swaps. \nFirst Element: " +
          str(a[0]) + "\nLast Element: " + str(a[-1]))
