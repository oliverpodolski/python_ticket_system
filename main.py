from database.db import DatabaseManager

db = DatabaseManager()

db.create_database()
db.create_table_tickets()
db.create_table_users()

logged_in_user_id = None

def start_menu():
    global logged_in_user_id

    while True:
        if logged_in_user_id == None:
            print("1 - Login")
            print("2 - Create User")
            print("3 - Exit")

            try:
                choice = int(input("\nWhat would you like to do?\n"))
            except ValueError:
                print("Please enter a valid Number!")
            if choice == 1:
                users = db.get_users()

                if not users:
                    print("There are no users. Please create a user first.")
                    return
                else:
                    login_user()
            elif choice == 2:
                create_user()
            elif choice == 3:
                break
            else:
                print("Please enter a valid option!")

def login_user():
    global logged_in_user_id

    users = db.get_users()

    for user in users:
        print(user)

    try:
        user_input = int(input("\nPlease enter your user ID to login: "))
    except ValueError:
        print("Please enter a valid Number!")

    for user in users:
        if user_input == user[0]:
            logged_in_user_id = user[0]
            print(f"\nLogged in as: {user[1]}")
            return loggedin_user_menu()
        else:
            print("Please Enter a valid choice!\n")

def create_user():
    name = input("Enter the first_name: ")
    surname = input("Enter the Surname: ")
    db.create_user(name, surname)
    print("User was created!")

def loggedin_user_menu():
    global logged_in_user_id
    print("1 - Create Ticket")
    print("2 - Show My Tickets")
    print("3 - Edit Ticket")
    print("4 - Logout")

    try:
        choice = int(input("\nWhat would you like to do?\n"))
    except ValueError:
        print("Please enter a valid Number!")

    if choice == 1:
        create_ticket()
    elif choice == 2:
        show_user_tickets()
    elif choice == 3:
        edit_ticket_status()
    elif choice == 4:
        logged_in_user_id = None
    else:
        print("Please enter a valid option!")
        return loggedin_user_menu()


def create_ticket():

    users = db.get_users()

    title = input("\nEnter the Title: \n")
    description = input("\nEnter the Description: \n")
    priority = int(input("\nEnter the Priority(1-10): \n"))
    status = "Open"
    print("Who would you like to assigne the Ticket:\n")
    for user in users:
        print(user)
    assigned_user = int(input("Enter the UserID: \n"))

    db.create_ticket(title, description, status, priority, assigned_user)

    print("Ticket was created!")
    return loggedin_user_menu()

def show_user_tickets():
    tickets = db.get_tickets()

    shown_tickets = 0
    for ticket in tickets:
        if ticket[5] == logged_in_user_id:
            print(f"ID: {ticket[0]}\nTitle: {ticket[1]}\nDescription: {ticket[2]}\nStatus: {ticket[3]}\nPriority: {ticket[4]}\n")
            shown_tickets += 1
    print("\n")
    if shown_tickets == 0:
        print("There are no tickets for you.")
    else:
        print(f"There are {shown_tickets} tickets for you.\n")
    return loggedin_user_menu()

def edit_ticket_status():

    tickets = db.get_tickets()

    if not tickets:
        print("There are no Tickets found for you.")
        return
    try:
        ticket_id = int(input("Enter the Ticket ID of the ticket you want to edit:\n"))
    except ValueError:
        print("Please enter a valid Number!")
    for ticket in tickets:
        if ticket_id == ticket[0] and logged_in_user_id == ticket[5]:
            print("Choose Status:")
            print("1 - Closed")
            print("2 - In Progress")
            print("3 - Open")

            try:
                choose = int(input("Please enter your change (number).\n"))
            except ValueError:
                print("Please enter a valid Number!")
            if choose == 1:
                db.update_ticket_status(ticket_id, "Closed")
                return loggedin_user_menu()
            if choose == 2:
                db.update_ticket_status(ticket_id, "In Progress")
                return loggedin_user_menu()
            if choose == 3:
                db.update_ticket_status(ticket_id, "Open")
                return loggedin_user_menu()
            print("change was made!")
    print("No ticket was found under this id!")
    return loggedin_user_menu()


start_menu()
