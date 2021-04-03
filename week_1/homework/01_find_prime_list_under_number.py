input = 20


def find_prime_list_under_number(number):
    is_prime_list = [True] * (number + 1)
    is_prime_list[0] = False
    is_prime_list[1] = False

    for x in range(2, number + 1):
        if is_prime_list[x]:
            for y in range(x * 2, number + 1, x):
                is_prime_list[y] = False
    prime_number_list = []
    for x in range(2, number + 1):
        if is_prime_list[x]:
            prime_number_list.append(x)
    return prime_number_list


result = find_prime_list_under_number(input)
print(result)
