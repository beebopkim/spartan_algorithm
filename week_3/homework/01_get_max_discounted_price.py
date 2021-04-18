shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort()
    coupons.sort()

    total = 0
    for i in range(len(shop_prices)):
        if len(coupons) > 0:
            percent = 1 - coupons.pop() / 100
        else:
            percent = 1
        total += shop_prices.pop() * percent
    return int(total)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.