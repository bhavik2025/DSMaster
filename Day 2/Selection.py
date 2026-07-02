lst = [51, 23, 9, 18, 61, 32]

def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print("Before Sort: ", lst)
print("After Sort: ", selection_sort(lst))