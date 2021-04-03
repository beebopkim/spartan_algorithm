input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    result = array[0]
    for x in array:
        if x > result:
            result = x
    return result


result = find_max_num(input)
print(result)

