Hotel Reservation System
Overview
This is a simple command-line Hotel Reservation System implemented in Python, designed to manage hotel room bookings and checkouts. The system allows users to view room statuses, book rooms based on preferred room types, and check out from rooms. It was coded by Qistina.
Features

Room Management: Tracks room availability and type (Single or Double).
Guest Booking: Allows guests to book available rooms, with an option to specify a preferred room type.
Checkout: Enables checking out from a booked room.
Room Status Display: Shows the current status of all rooms (booked or available).

Prerequisites

Python 3.x installed on your system.

How to Run

Save the hotel_guest_reservation_system.py file in your working directory.
Open a terminal or command prompt and navigate to the directory containing the file.
Run the program using the command:python hotel_guest_reservation_system.py


Follow the on-screen menu to interact with the system.

Usage
Upon running the program, a menu will be displayed with the following options:

View all rooms: Displays the status and type of all rooms.
Book a room: Prompts for guest name, contact, and optional preferred room type (Single or Double). Books the first available room matching the criteria.
Check out: Prompts for a room number to check out, freeing the room if it was booked.
Exit: Terminates the program.

Code Structure

Room Class:
Attributes: room_number, room_type, is_booked.
Methods: book_room(), checkout(), display_info().


Guest Class:
Attributes: name, contact.
Method: request_room() to book a room based on availability and optional type preference.


Main Function:
Initializes a list of rooms (at least 5, with Single and Double types).
Provides a menu-driven interface for user interaction.



Example Interaction
=== Hotel Reservation System ===
1. View all rooms
2. Book a room
3. Check out
4. Exit
Enter your choice (1-4): 1

Room Status:
Room 101 (Single): Available
Room 102 (Single): Available
Room 103 (Double): Available
Room 104 (Double): Available
Room 105 (Single): Available
Room 106 (Double): Available

Notes

The system currently supports a fixed list of rooms (101–106) defined in the main() function.
Room numbers must be entered as integers during checkout.
Invalid inputs (e.g., non-numeric room numbers or invalid menu choices) are handled with appropriate error messages.
The system does not persist data; all bookings are reset when the program terminates.

Author
Coded by Qistina.
License
This project is for educational purposes and does not include a specific license.</x
