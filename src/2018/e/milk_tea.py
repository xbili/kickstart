def milk_tea(n, m, p, prefs, forbidden):
    """
    Returns the least number of complaints that Shakti can get from buying a
    single cup of coffee because he was lazy.

    Seriously, how hard can it be to just write down the orders?
    """
    t = set([('', 0)])
    for i in range(p):
        best = []
        for item, complaints in t:
            # Append 1 and 0
            one, zero = item + '1', item + '0'

            # Check complaints
            one_complaints = sum(pref[i] != '1' for pref in prefs) + complaints
            zero_complaints = sum(pref[i] != '0' for pref in prefs) + complaints

            # Append to current best
            best += [(one, one_complaints), (zero, zero_complaints)]

        # Take only the smallest 101
        t = set(sorted(best, key=lambda x: x[1])[:101])

    filtered = set(item for item in t if item[0] not in forbidden)
    selected = sorted(list(filtered), key=lambda x: x[1])[0]
    return selected[1]

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, m, p = [int(s) for s in input().split(" ")]
        prefs = [input() for _ in range(n)]
        forbidden = [input() for _ in range(m)]
        print('Case #{}: {}'.format(i, milk_tea(n, m, p, prefs, forbidden)))
