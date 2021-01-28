# python 3.9
USD_COIN_SURCULATION = [25, 10, 5, 1]
missing_coins_from_register = [5]


def minimal_number_of_coins(summ: int, coins_in_circulation: list, missing_coins: list = None) -> int:
    if missing_coins is None:
        missing_coins = []

    # creates a list without the missing coins
    coins = [c for c in coins_in_circulation if c not in missing_coins]

    # store the number of coin needed. It is equal to the coins list
    list_number_coins = []

    # stores the current coins who will be subtracted from the sum
    current_list_coins = []

    # list of sums who will be subtracted
    list_sum = [summ] * len(coins)

    for i in range(len(coins)):
        number_coins = 0
        current_list_coins.insert(0, coins.pop())
        while list_sum[i]:
            for coin in current_list_coins:
                while list_sum[i] >= coin:
                    if list_sum[i] % coin >= 0:
                        list_sum[i] -= coin
                        number_coins += 1
                        if missing_coins:
                            if list_sum[i] >= coin + missing_coins[0] and list_sum[i] <= coin + missing_coins[0] + 4:
                                break

        list_number_coins.append(number_coins)
    return min(list_number_coins)


# test for all numbers
for x in range(101):
    all = minimal_number_of_coins(x, USD_COIN_SURCULATION)
    without_five = minimal_number_of_coins(x, USD_COIN_SURCULATION, missing_coins_from_register)

    print(f"sum of {x} = {all=}, {without_five=}")
