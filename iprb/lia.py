import sys

parts = sys.stdin.readline().strip().split()
k = int(parts[0])
n = int(parts[1])

p1 = 0.
p2 = 1.
p3 = 0.

for i in xrange(k):
    p1, p2, p3 = p1/2 + p2/4, (p1 + p2 + p3)/2, p2/4 + p3/2

fact = [1]
for i in xrange(1, 200):
    fact.append( fact[-1]*i )

res = 0
p2 = p2*p2
print p2
for i in xrange(n, 2**k + 1):
    c = fact[2**k]/fact[i]/fact[2**k - i]

    def power(x, n):
        res = 1.
        for j in xrange(n):
            res *= x
        return res

    res += c*power(p2, i)*power((1. - p2), (2**k - i))
print res