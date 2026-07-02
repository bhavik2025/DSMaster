bookWait = [2,8,6,4,2,3,1,5,6]

def arrange_books(lst):
    count = 0
    for i in range(len(lst)):
        count += 1
        flag = False
        for j in range(len(lst) - i - 1):
            count += 1
            if lst[j] > lst[j+1]:
                flag = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if flag:
            break
    print(count)
    return lst

print("Before Sort: ", bookWait)
print("After Sort: ",arrange_books(bookWait))