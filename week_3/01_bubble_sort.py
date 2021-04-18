input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    for x in range(0, len(array) - 1):
        for y in range(0, len(array) - 1 - x):
            if array[y] > array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
    return


bubble_sort(input)

print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
