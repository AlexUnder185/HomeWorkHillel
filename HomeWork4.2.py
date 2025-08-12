lst = [0, 1, 7, 2, 4, 8]

even_lst = lst[::2]
total = sum(even_lst)

if not lst: last_element = 0
else: last_element = lst[-1]

print(total * last_element)
