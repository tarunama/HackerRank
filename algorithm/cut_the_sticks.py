not_need = input()
s_cuts = []
ns = [int(n) for n in raw_input().split()]


def ans(ns):
    minimum = min(ns)
    s_cuts.append(len(ns))
    ns = [n - minimum for n in ns if n > minimum]
    if len(ns) > 0:
        ans(ns)
    else:
        for n in s_cuts:
            print n

ans(ns)
