def dig_pow(n, p):
    # your code
    nums = [i for i in str(n)]
    sum = 0
    for i in nums:
        sum += int(i) ** p
        p += 1
    k = sum // n
    if n * k == sum:
        return k
    else:
        return -1

