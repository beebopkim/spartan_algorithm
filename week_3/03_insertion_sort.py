input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            for j in range(i, 0, -1):
                if array[j - 1] > array[j]:
                    array[j - 1], array[j] = array[j], array[j - 1]
                else:
                    break
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
