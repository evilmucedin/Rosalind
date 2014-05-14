import sys

name = ""
count = 0
gCount = 0
maxRatio = 0.
maxName = ""

def updateMax():
    global maxRatio, maxName, count, gCount
    if count > 0:
        ratio = float(gCount)/count
        if ratio > maxRatio:
            maxRatio = ratio
            maxName = name
    count = 0
    gCount = 0

for line in sys.stdin:
    line = line.strip()
    if len(line) > 0:
        if line[0] == ">":
            updateMax()
            name = line[1:]
        else:
            for c in line:
                if c == 'G' or c == 'C':
                    count += 1
                    gCount += 1
                elif c == 'A' or c == 'T':
                    count += 1

updateMax()

print maxName
print maxRatio*100.