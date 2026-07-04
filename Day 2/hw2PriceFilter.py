prices = [25000, 32000, 40000, 48000, 50000, 50000, 55000, 60000, 70000]

target = int(input("Enter target price: "))

low = 0
high = len(prices) - 1
answer = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

if answer != -1:
    print("First product >= target is at index:", answer)
    print("Price:", prices[answer])
else:
    print("No product found with price >= target.")