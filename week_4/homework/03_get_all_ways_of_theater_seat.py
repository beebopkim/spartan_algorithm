seat_count = 9
vip_seat_array = [4, 7]

fibo_memo = {
    1: 1,
    2: 2
}


def fibo(n, memo):
    if n in memo:
        return memo[n]

    nth_fibo = fibo(n - 1, memo) + fibo(n - 2, memo)
    memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    result = 1
    local_total = total_count - len(fixed_seat_array)
    for i, fs in enumerate(fixed_seat_array):
        #print("total count {}".format(aaa))
        #print(i, fs, len(fixed_seat_array))
        if i == 0:
            lo = 1
            hi = fs - 1
            result *= fibo((hi - lo) + 1, fibo_memo)
            local_total -= (hi - lo) + 1
        else:
            lo = prev_fs + 1
            hi = fs - 1
            result *= fibo((hi - lo) + 1, fibo_memo)
            local_total -= (hi - lo) + 1
        if i == len(fixed_seat_array) - 1:
            lo = fs + 1
            hi = seat_count
            result *= fibo((hi - lo) + 1, fibo_memo)
            local_total -= (hi - lo) + 1

        prev_fs = fs
    return int(result)

# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
