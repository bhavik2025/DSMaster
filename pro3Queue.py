class smartPrint():
    def __init__(self, max_size):
        self.urgentQueue = []
        self.normalQueue = []
        self.max_size = max_size
    
    def add_job(self, job, priority="normal"):
        if priority == "urgent":
            if len(self.urgentQueue) < self.max_size:
                self.urgentQueue.append(job)
            else:
                print("Urgent queue is full. Cannot add job.")
        elif priority == "normal":
            if len(self.normalQueue) < self.max_size:
                self.normalQueue.append(job)
            else:
                print("Normal queue is full. Cannot add job.")
        else:
            print("Invalid priority. Use 'urgent' or 'normal'.")

    def process_job(self):
        if self.urgentQueue:
            job = self.urgentQueue.pop(0)
            print(f"Processing urgent job: {job}")
        elif self.normalQueue:
            job = self.normalQueue.pop(0)
            print(f"Processing normal job: {job}")
        else:
            print("No jobs to process.")

sp = smartPrint(max_size=5)

while True:
    print("\n * Menu *")
    print("1. Add Jon")
    print("2. Process Job")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        job = input("Enter job name: ")
        priority = input("Enter priority (normal/urgent): ")
        sp.add_job(job, priority)
    elif choice == 2:
        sp.process_job()
    elif choice == 3:
        print("Exiting...")
        break