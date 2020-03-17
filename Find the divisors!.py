def divisors(integer):
    Div = [x for x in range(2,integer) if integer % x == 0]
    if Div == [] and integer % integer == 0:
        return "{} is prime".format(integer)
    else:
        return Div

