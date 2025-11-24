# Film-ticket-booking-system
🎬 Movie Ticket Booking System – Python CLI Project

Welcome to my Movie Ticket Booking System built entirely using Python!
This program lets users browse movies, book tickets, view bookings, and generate a bill — all through a simple command-line interface.

📌 Project Overview

This Python program simulates a movie ticket booking system.
It includes features such as:

🎥 Displaying available films

🎟 Booking tickets

📄 Viewing your bookings

💰 Generating a detailed bill with GST

🪑 Tracking available seats

🛠️ Features Explained
🎥 1. Show Available Films

The show_films() function displays all movies with:

Movie name

Ticket price

Unique ID for selecting a movie

A clean table-like format makes it easy to browse options.

🎟 2. Book Tickets

The core function book_ticket() allows users to:

Select a film using its number

Check ticket price

View available seats

Choose how many tickets to book

It also:

Validates user input

Prevents booking more seats than available

Updates seat counts and booking records

📄 3. View Bookings

The function view_bookings() displays all tickets the user has booked so far.
If no tickets exist, it politely informs the user.

🧾 4. Generate Bill

The bill() function prints a clean invoice including:

Movies booked

Quantity

Subtotals

GST (5%)

Final total amount

🔁 5. Continuous Menu Loop

The program uses a while True: loop to keep the system running until the user chooses to exit.

Options include:

1. Show films
2. Book tickets
3. View bookings
4. Generate bill
5. Exit

📂 Data Structures Used
📘 Dictionaries

films → Stores movie names and prices

seats → Tracks seat availability

F → Stores user bookings

Dictionaries make it easy to fetch movie details and update records.

⚠️ Known Issues & Notes

There is a small bug in the bill() function:

The variable C (total cost) is used before being defined.

And the line fetching the movie price uses an incorrect loop.

If you want, I can fix the entire code for you! 😊

🚀 How to Run

Just run the script using Python:

python movie_booking.py


Make your selections through the terminal menu.