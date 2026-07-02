class TollPlaza:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, vehicle):
        if self.is_full():
            print("Toll plaza is full. Vehicle must wait.")
            return
        self.queue[self.rear] = vehicle
        self.rear = (self.rear + 1)
        self.size += 1
        print(f"Vehicle '{vehicle}' has entered the toll plaza.")

    def dequeue(self):
        if self.is_empty():
            print("Toll plaza is empty. No vehicles to process.")
            return None
        vehicle = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1)
        self.size -= 1
        print(f"Vehicle '{vehicle}' has exited the toll plaza.")
        return vehicle

    def display(self):
        if self.is_empty():
            print("Toll plaza is empty.")
            return
        print("Vehicles in the toll plaza:")
        index = self.front
        for _ in range(self.size):
            print(f"- {self.queue[index]}")
            index = (index + 1) % self.capacity

while True:
    toll_plaza = TollPlaza()
    print("\nToll Plaza Simulation")
    print("1. Enter Vehicle")
    print("2. Exit Vehicle")
    print("3. Display Vehicles")
    print("4. Exit Simulation")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        vehicle = input("Enter vehicle name to enter: ")
        toll_plaza.enqueue(vehicle)

    elif choice == 2:
        toll_plaza.dequeue()

    elif choice == 3:
        toll_plaza.display()

    elif choice == 4:
        print("Exiting simulation.")
        break

    else:
        print("Invalid choice. Please try again.")