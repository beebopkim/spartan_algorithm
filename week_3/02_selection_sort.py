input = [4, 6, 2, 9, 1]


def selection_sort(array):
    for i in range(len(array)):
        min_pos = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_pos]:
                min_pos = j
        array[i], array[min_pos] = array[min_pos], array[i]
    return

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!