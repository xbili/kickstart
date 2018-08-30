from collections import Counter


def yogurt(n, k, arr):
    """Returns the largest number of yogurts that Lucy can consume."""
    # Since k >= 1, Lucy will take at most N days to clear ALL of the yogurt.
    arr = [item if item < n else n for item in arr]

    # Count how many yogurts expire on each day
    ctr = Counter(arr)

    # Work backwards from day N to day 1, moving leftover cups in each day
    # to a day earlier
    for day in reversed(range(1, n+1)):
        ctr[day-1] += max(0, ctr[day] - k)

    return n - ctr[0]

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        arr = [int(s) for s in input().split(" ")]
        print('Case #{}: {}'.format(i, yogurt(n, k, arr)))
