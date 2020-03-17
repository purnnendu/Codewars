def nb_year(p0, percent, aug, p):
    n = 0
    np = percent / 100
    while p0 < p:
        p0 += aug + int(p0 * np)
        n += 1
    return n

