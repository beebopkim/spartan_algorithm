
input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    first_char = string[0]
    prev_char = first_char

    cnt = 0
    for x in string[1:]:
        if x != first_char and x != prev_char:
            cnt += 1
        prev_char = x

    return cnt


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
