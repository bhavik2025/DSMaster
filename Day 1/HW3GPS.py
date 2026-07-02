class GPSNavigation:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def visit(self, place):
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]
        self.history.append(place)
        self.current_index += 1

    def back(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.history[self.current_index]
        else:
            return None

    def forward(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            return self.history[self.current_index]
        else:
            return None

    def current_place(self):
        if self.current_index >= 0:
            return self.history[self.current_index]
        else:
            return None

gps = GPSNavigation()

while True:
    print("\nGPS Navigation Simulation")
    print("1. Visit Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Current Place")
    print("5. Exit Simulation")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        place = input("Enter place to visit: ")
        gps.visit(place)
        print(f"Visited '{place}'.")

    elif choice == 2:
        previous_place = gps.back()
        if previous_place:
            print(f"Went back to '{previous_place}'.")
        else:
            print("No previous place to go back to.")

    elif choice == 3:
        next_place = gps.forward()
        if next_place:
            print(f"Went forward to '{next_place}'.")
        else:
            print("No forward place to go to.")

    elif choice == 4:
        current_place = gps.current_place()
        if current_place:
            print(f"Current place is '{current_place}'.")
        else:
            print("No current place.")
    
    elif choice == 5:
        print("Exiting simulation.")
        break

    else:
        print("Invalid choice. Please try again.")