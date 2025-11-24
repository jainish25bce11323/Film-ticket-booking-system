films = {
    1: ("Vertigo", 440),
    2: ("Days of Heaven", 280),
    3: ("Barry Lyndon", 1050),
    4: ("Ran", 350)
}
seats = {
    "Vertigo": 115,
    "Days of Heaven": 80,
    "Barry Lyndon": 95,
    "Ran": 85
}
F = {}
def header():
    print("\n" + "="*40)
    print("MOVIE TICKET BOOKING SYSTEM")
    print("="*30)
def show_films():
    print("\nAvailable Films:")
    print("-"*30)
    for num, (name, price) in films.items():
        print(f"{num}. {name:20} ₹{price}")
    print("-"*30)
def book_ticket():
    show_films()
    try:
        A = int(input("Enter the film number: "))
        if A not in films:
            print("Invalid choice!")
            return
        name, price = films[A]
        print(f"\nFilm selected: {name}")
        print(f"Price of ticket: ₹{price}")
        print(f"Seats Available currently: {seats[name]}")
        E = int(input("Number of tickets you'd like to book: "))
        if E <= 0:
            print("Invalid quantity!!!")
            return
        if E > seats[name]:
            print("enough seats available!!!")
            return
        seats[name] = E
        F[name] = F.get(name, 0) + E
        print(f"\n{E} ticket(s) booked for {name}.")
    except ValueError:
        print("Kindly enter a valid number.")
def view_bookings():
    if not F:
        print("\nNo tickets have been booked yet")
        return
    print("\nYour Bookings:")
    print("-"*40)
    for name, E in F.items():
        print(f"{name:25} Tickets:{E}")
def bill():
    if not F:
        print("\nNo bookings have been found yet unfortunaely.")
        return
    print("\n"+"="*40)
    print("BILL")
    print("="*40)
    subtotal = 0
    for name, E in F.items():
        price = next(p for n, p in films.values() if n == name)
        D = E * price
        C += D
        print(f"{name:25} x {E} = ₹{D}")
    gst = C * 0.05
    B = C + gst
    print("-"*40)
    print(f"Subtotal:₹{C}")
    print(f"GST (5%):₹{gst:.2f}")
    print("="*30)
    print(f"TOTAL AMOUNT:₹{B:.2f}")
    print("="*30)
def main():
    header()
    while True:
        print("\n1 Show films available")
        print("2 Book tickets for films")
        print("3 View bookings for your films")
        print("4 Generate bill for your choices")
        print("5 exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_films()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            bill()
        elif choice == "5":
            print("\nThank you for using the system. Hoping you'd come next time aswell!")
            break
        else:
            print("INVALIDDD !!!!!! Try again")
if __name__ == "__main__":
    main()