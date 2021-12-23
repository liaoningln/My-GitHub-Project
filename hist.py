def distribute(histogram, k):
    list1 = [0] * k
    mini = min(histogram)
    maxi = max(histogram)
    gap = (maxi - mini) / k
    for i in histogram:
        index = int((i - mini) / gap)
        if (i - mini) != 0 and (i - mini) % gap == 0:
            index -= 1
        list1[int(index)] += 1
    return list1


assert distribute([1.25, 1, 2, 1.75], 2) == [2, 2]
