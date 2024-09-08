def getMaxToys(prices, money):
    n = len(prices)
    max_toys = 0
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += prices[end]

        while current_sum > money:
            current_sum -= prices[start]
            start += 1

        max_toys = max(max_toys, end - start + 1)

    return max_toys


n = int(input().strip())
prices = list(map(int, input().strip().split()))
money = int(input().strip())


print(getMaxToys(prices, money))