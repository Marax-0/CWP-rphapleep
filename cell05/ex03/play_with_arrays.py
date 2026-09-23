original_arr = [2,8,9,48,8,22,-12,2]
new_arr = set([num + 2 for num in original_arr if num > 5])

print(original_arr)
print(new_arr)
