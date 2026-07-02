# C2) The Scholarship Ranker A college must give scholarships to the top 3 scorers. The coordinator scans the entire marksheet, finds the highest scorer, moves them to position 1. Then scans the remaining students for the next highest, and so on. Each pass = one full scan to select the minimum/maximum.

marks = [95,85,99,75,47,86,97,84,86,100]

def get_First_3(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
    return lst[-1:-4:-1]

print("Result Of All: ",marks)
pos = get_First_3(marks)
print("Position 1: ",pos[0])
print("Position 2: ",pos[1])
print("Position 3: ",pos[2])