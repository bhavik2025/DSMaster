class conveyor:
    def __init__(self):
        self.slots = [None] * 8 

    def check_slot(self, slot_number):
        if 0 <= slot_number < len(self.slots):
            return self.slots[slot_number]
        raise IndexError("Slot number out of range. Must be between 0 and 7.")

    def find_product(self, product):
        for index, item in enumerate(self.slots):
            if item == product:
                return index
        return -1
    
    def update_slot(self, slot_number, product):
        if 0 <= slot_number < len(self.slots):
            self.slots[slot_number] = product
        else:
            raise IndexError("Slot number out of range. Must be between 0 and 7.")

    def is_full(self):
        return all(slot is not None for slot in self.slots)

while True:
    conveyor_belt = conveyor()
    print("Conveyor Belt System")
    print("1. Check Slot")
    print("2. Find Product")
    print("3. Update Slot")
    print("4. Check if Full")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        slot_number = int(input("Enter slot number (0-7): "))
        try:
            product = conveyor_belt.check_slot(slot_number)
            if product is not None:
                print(f"Slot {slot_number} contains: {product}")
            else:
                print(f"Slot {slot_number} is empty.")
        except IndexError as e:
            print(e)

    elif choice == '2':
        product = input("Enter product name to find: ")
        index = conveyor_belt.find_product(product)
        if index != -1:
            print(f"Product '{product}' found in slot {index}.")
        else:
            print(f"Product '{product}' not found on the conveyor belt.")

    elif choice == '3':
        slot_number = int(input("Enter slot number (0-7): "))
        product = input("Enter product name to place in the slot: ")
        try:
            conveyor_belt.update_slot(slot_number, product)
            print(f"Slot {slot_number} updated with product '{product}'.")
        except IndexError as e:
            print(e)

    elif choice == '4':
        if conveyor_belt.is_full():
            print("The conveyor belt is full.")
        else:
            print("The conveyor belt is not full.")

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")