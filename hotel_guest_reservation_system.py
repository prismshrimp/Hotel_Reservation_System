# Hotel Reservation System

class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_booked = False

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def checkout(self):
        if self.is_booked:
            self.is_booked = False
            return True
        return False

    def display_info(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number} ({self.room_type}): {status}"

class Guest:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def request_room(self, rooms, preferred_type=None):
        for room in rooms:
            if not room.is_booked and (preferred_type is None or room.room_type == preferred_type):
                if room.book_room():
                    return f"{self.name} successfully booked {room.display_info()}"
        return f"No available {preferred_type if preferred_type else 'room'} found."

def main():
    # Create a list of at least 5 rooms
    rooms = [
        Room(101, "Single"),
        Room(102, "Single"),
        Room(103, "Double"),
        Room(104, "Double"),
        Room(105, "Single"),
        Room(106, "Double")
    ]

    while True:
        print("\n=== Hotel Reservation System ===")
        print("1. View all rooms")
        print("2. Book a room")
        print("3. Check out")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nRoom Status:")
            for room in rooms:
                print(room.display_info())

        elif choice == "2":
            name = input("\nEnter guest name: ")
            contact = input("Enter guest contact: ")
            room_type = input("Enter preferred room type (Single/Double, or press Enter for any): ").strip()
            room_type = room_type if room_type in ["Single", "Double"] else None
            guest = Guest(name, contact)
            print(guest.request_room(rooms, room_type))

        elif choice == "3":
            room_number = input("\nEnter room number to check out: ")
            try:
                room_number = int(room_number)
                for room in rooms:
                    if room.room_number == room_number:
                        if room.checkout():
                            print(f"Room {room_number} checked out successfully.")
                        else:
                            print(f"Room {room_number} is already available.")
                        break
                else:
                    print(f"Room {room_number} not found.")
            except ValueError:
                print("Invalid room number. Please enter a number.")

        elif choice == "4":
            print("Exiting system. Goodbye! We hope to see you soon!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()