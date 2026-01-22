lst = [1, 2, 2, 3, 4, 4, 5]

result = []
for item in lst:
    if item not in result:
        result.append(item)

print(result)
