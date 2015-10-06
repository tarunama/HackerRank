not_need = input()
sizes = [n for n in raw_input().split()]
customers = int(input())

total = 0
for c in customers:
    size, price = raw_input().split()
    if size in sizes:
        sizes.remove(size)
        total += price

print total
