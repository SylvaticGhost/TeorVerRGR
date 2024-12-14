def derangements(k):
    if k == 0:
        return 1
    if k == 1:
        return 0
    return (k - 1) * (derangements(k - 1) + derangements(k - 2))