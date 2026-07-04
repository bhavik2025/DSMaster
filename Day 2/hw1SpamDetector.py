# Linear Search

blacklist = ["SP101", "SP205", "SP330", "SP450", "SP500"]

target = input("Enter Sender ID: ")

found = False

for sender in blacklist:
    if sender == target:
        found = True
        break

if found:
    print("Spam Sender Found!")
else:
    print("Sender Not Found.")