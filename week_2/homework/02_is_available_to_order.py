shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    order_possible = True
    for order in orders:
        if not (order in menus):
            order_possible = False
            break

    return order_possible


result = is_available_to_order(shop_menus, shop_orders)
print(result)