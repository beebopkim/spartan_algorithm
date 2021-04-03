input = "abacabade"
#input = "abadabac"


def find_not_repeating_character(string):
    occur_list = [0] * 26
    for x in string:
        if x.isalpha():
            occur_list[ord(x) - ord('a')] += 1
    min_occur_char_list = []
    for i, occur in enumerate(occur_list, start = 0):
        if occur == 1:
            min_occur_char_list.append(chr(ord('a') + i))
    print(min_occur_char_list)
    for x in string:
        if x in min_occur_char_list:
            return x
    return '_'


result = find_not_repeating_character(input)
print(result)