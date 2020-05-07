import sys

total = 0
n = 0

for line in sys.stdin:
    number = float(line)
    total += number
    n += 1
    
print("average is", total / n)
