mobile_waitlist = [2, 5, 8, 12]
counter_waitlist = [1, 4, 7, 10, 15]

merged = []

i = 0
j = 0

while i < len(mobile_waitlist) and j < len(counter_waitlist):
    if mobile_waitlist[i] < counter_waitlist[j]:
        merged.append(mobile_waitlist[i])
        i += 1
    else:
        merged.append(counter_waitlist[j])
        j += 1

while i < len(mobile_waitlist):
    merged.append(mobile_waitlist[i])
    i += 1

while j < len(counter_waitlist):
    merged.append(counter_waitlist[j])
    j += 1

print("Merged Waitlist:", merged)