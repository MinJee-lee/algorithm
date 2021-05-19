s = input()
result = int(s[0])
for i in range(1, len(s)):
    value = int(s[i])
    if result == 0 or result == 1 or value == 0 or value == 1:
        result += value
    else:
        result *= value
print(result)