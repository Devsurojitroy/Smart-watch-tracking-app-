import random
import time
import datetime

class Smartwatch:
    def __init__(self, user_name):
        self.user_name = user_name
        self.heart_rate = 0
        self.steps = 0
        self.calories_burned = 0
        self.sleep_duration = 0
        self.data = []

    def generate_heart_rate(self):
        self.heart_rate = random.randint(60, 100)

    def generate_steps(self):
        self.steps += random.randint(100, 500)

    def generate_calories(self):
        self.calories_burned += random.uniform(0.5, 5.0)

    def generate_sleep_duration(self):
        self.sleep_duration = random.uniform(4, 8)

    def record_data(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.generate_heart_rate()
        self.generate_steps()
        self.generate_calories()
        self.generate_sleep_duration()
        
        data_entry = {
            "timestamp": timestamp,
            "heart_rate": self.heart_rate,
            "steps": self.steps,
            "calories_burned": round(self.calories_burned, 2),
            "sleep_duration": round(self.sleep_duration, 2),
        }
        
        self.data.append(data_entry)
        print(f"Data recorded at {timestamp}")

    def show_stats(self):
        print("\n--- Current Stats ---")
        print(f"User: {self.user_name}")
        print(f"Heart Rate: {self.heart_rate} bpm")
        print(f"Steps: {self.steps}")
        print(f"Calories Burned: {round(self.calories_burned, 2)} kcal")
        print(f"Sleep Duration: {round(self.sleep_duration, 2)} hours")
        print("----------------------\n")

    def show_history(self):
        print("\n--- Activity History ---")
        for entry in self.data:
            print(entry)
        print("------------------------\n")

def main():
    user_name = input("Enter your name: ")
    watch = Smartwatch(user_name)
    
    while True:
        print("\n1. Record Data\n2. Show Stats\n3. Show History\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            watch.record_data()
        elif choice == '2':
            watch.show_stats()
        elif choice == '3':
            watch.show_history()
        elif choice == '4':
            print("Exiting the app. Stay healthy!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
