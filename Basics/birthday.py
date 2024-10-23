candles = (1,2,3,5)

count = 0
for x in candles:
    count += 1
i = 0
for i in range(count):
    big = candeles[i]
    if candles[i] > big:
        big = candles[i]
    
for x in candles:
    if x == big:
        count += 1
print(count)