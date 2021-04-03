def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for x in string:
        if x.isalpha():
            alphabet_occurrence_array[ord(x) - ord('a')] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))