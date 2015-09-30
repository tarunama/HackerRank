from itertools import product

list_A = [int(n) for n in raw_input().split()]
list_B = [int(n) for n in raw_input().split()]

print " ".join(map(str, list(product(list_A, list_B))))
