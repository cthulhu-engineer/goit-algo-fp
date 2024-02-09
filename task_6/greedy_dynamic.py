def greedy_algorithm(items, budget):
    """
    Selects items greedily based on the cost-to-calories ratio until the budget is exceeded.

    :param items: A dictionary of items, where the key is the item name and the value is a dictionary containing
                  the item's cost and calories. The dictionary should have the following structure:
                  {
                      'item_name': {
                          'cost': item_cost,
                          'calories': item_calories
                      }
                  }
    :param budget: The maximum budget to spend.
    :return: A tuple containing a list of chosen item names and the total calories of the chosen items.
    """
    cost_per_calorie = {item: (info['calories'] / info['cost']) for item, info in items.items()}
    sorted_items = sorted(cost_per_calorie.items(), key=lambda x: x[1], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, _ in sorted_items:
        if total_cost + items[item]['cost'] <= budget:
            chosen_items.append(item)
            total_cost += items[item]['cost']
            total_calories += items[item]['calories']

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    """
    Finds the optimal selection of items with maximum total calories within a given budget using dynamic programming.

    :param items: A dictionary where the keys are the names of the items and the values are dictionaries
        with 'cost' and 'calories' representing the cost and calories of the item, respectively.
    :param budget: The maximum budget available.
    :return: A tuple containing a list of selected items and the maximum total calories.
    """
    dp = [[0 for x in range(budget + 1)] for x in range(len(items) + 1)]

    item_list = list(items.keys())

    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            if items[item_list[i - 1]]['cost'] <= w:
                dp[i][w] = max(items[item_list[i - 1]]['calories'] + dp[i - 1][w - items[item_list[i - 1]]['cost']],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    n = len(items)
    chosen_items = []

    while w >= 0 and n >= 0:
        if dp[n][w] != dp[n - 1][w]:
            chosen_items.append(item_list[n - 1])
            w -= items[item_list[n - 1]]['cost']
        n -= 1

    return chosen_items, dp[-1][-1]


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    greedy_choice, greedy_calories = greedy_algorithm(items, budget)
    print("Greedy Algorithm:")
    print("Chosen items:", greedy_choice)
    print("Total calories:", greedy_calories)

    dp_choice, dp_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming:")
    print("Chosen items:", dp_choice)
    print("Total calories:", dp_calories)
