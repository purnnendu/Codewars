def high_and_low(numbers):
    # ...
    new = [int(i) for i in numbers.split()]
    res = sorted(new)
    return "{} {}".format(res[-1], res[0])

