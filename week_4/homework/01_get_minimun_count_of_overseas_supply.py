import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    date_index = 0
    flower_usage_per_day = 1
    max_heap = []
    supply_count = 0

    while stock < flower_usage_per_day * k:
        for i in range(date_index, len(dates)):
            if dates[i] * flower_usage_per_day <= stock:
                heapq.heappush(max_heap, - supplies[i])
                #print("date: {}, stock {}".format(i, stock))
            else:
                date_index = i
                break
        supply_count += 1
        t = -heapq.heappop(max_heap)
        #print(t)
        stock += t * flower_usage_per_day
    return supply_count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))