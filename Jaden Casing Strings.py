def to_jaden_case(string):
    new = ""
    for i in string.split():
        new += i[0].upper() + i[1:] + " "
    return new.strip()

#def to_jaden_case(string):
    #return " ".join(w.capitalize() for w in string.split())
