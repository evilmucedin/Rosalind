import sys

line = sys.stdin.readline().strip()
parts = line.split()
k = float(parts[0])
m = float(parts[1])
n = float(parts[2])
sum = k + m + n
print (k*(k - 1 + m + n) + m*(k + 3.*(m - 1)/4 + n/2) + n*(k + m/2))/sum/(sum - 1)