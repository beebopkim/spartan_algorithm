input = "abcba"

def is_palindrome(string):
    is_p = True

    for i in range(0, len(string) // 2):
        if is_p and string[i] != string[- (i + 1)]:
            is_p = False
            break
    return is_p


print(is_palindrome(input))