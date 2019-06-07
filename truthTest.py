for A in (False, True):
    for B in (False, True):
        for C in (False, True):
            c = (A and B and C) or (A and B and not C) or (
                not A and B and C) or (A and not B and C)
            s = (A and B and C) or (A and not B and not C) or (
                not A and B and not C) or (not A and not B and C)
            print(f"{A} --- {B} --- {C} --- Carry: {c} --- Sum: {s}")
