lst = [51, 23, 9, 18, 61, 32]

def bubble_sort(lst):
    count = 0
    for i in range(len(lst)):
        count += 1
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                count += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(count)
    return lst

print("Before Sort: ", lst)
print("After Sort: ",bubble_sort(lst))
