N = input()
d = {}

for i in xrange(N):
    name, score1, score2, score3 = raw_input().split()
    d[name] = [score1, score2, score3]

required_name = raw_input()
_sum = reduce(lambda x, y: x + y, [float(n) for n in d[required_name]])
print "{0:.2f}".format(_sum / len(d[required_name]))
