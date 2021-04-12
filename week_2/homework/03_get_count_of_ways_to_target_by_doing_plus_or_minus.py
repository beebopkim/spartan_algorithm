numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    return count_helper(array, target, 0)


def count_helper(array, target, result):
    if len(array) == 0:
        if result == target:
            return 1
        else:
            return 0
    else:
        return count_helper(array[1:], target, result + array[0]) \
               + count_helper(array[1:], target, result - array[0])




print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!