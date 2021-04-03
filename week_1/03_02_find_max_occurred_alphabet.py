input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for x in string:
        if x.isalpha():
            alphabet_occurrence_array[ord(x) - ord('a')] += 1

    max_pos = 0
    max_val = alphabet_occurrence_array[0]

    pos = 0
    for x in alphabet_occurrence_array:
        if x > max_val:
            max_val = x
            max_pos = pos
        pos += 1

    return chr(ord('a') + max_pos)


result = find_max_occurred_alphabet(input)
print(result)