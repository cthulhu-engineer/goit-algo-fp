import numpy as np
import matplotlib.pyplot as plt


def roll_dice(num_rolls):
    """
    Simulate rolling of two dice.

    :param num_rolls: The number of times to roll the dice.
    :type num_rolls: int
    :return: The sum of the two dice for each roll.
    :rtype: numpy.ndarray
    """
    # Симуляція кидків
    roll1 = np.random.randint(1, 7, size=num_rolls)
    roll2 = np.random.randint(1, 7, size=num_rolls)
    sums = roll1 + roll2
    return sums


def calculate_probabilities(sums):
    """

    Calculate probabilities for each sum.

    :param sums: A numpy array of sums.
    :return: An array of probabilities for each sum.

    """
    # Підрахунок кількості кожної суми
    counts = np.bincount(sums)
    probabilities = counts / np.sum(counts)
    return probabilities


if __name__ == '__main__':

    num_rolls = 1000000

    sums = roll_dice(num_rolls)
    probabilities = calculate_probabilities(sums)

    plt.bar(range(2, len(probabilities)), probabilities[2:], tick_label=range(2, len(probabilities)))
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.show()

    for sum_value, probability in enumerate(probabilities[2:], start=2):
        print(f"Сума: {sum_value}, Ймовірність: {probability * 100:.2f}%")
