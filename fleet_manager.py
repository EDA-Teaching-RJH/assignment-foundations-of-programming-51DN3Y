def main():
    '''Main function to run the fleet manager program. Displays menu and prompts user for input until they choose to exit.'''
    print("\nWelcome to Fleet Manager System")
    name, rank, division, id, valid_rank, student_name = init_database() 

    while True:
        opt = display_menu()
        if opt == 1:
            add_member(name, rank, division, id, valid_rank)
        elif opt == 2:
            remove_member(name, rank, division, id)
        elif opt == 3:
            update_rank(rank, id)
        elif opt == 4:
            display_roster(name, rank, division, id)
        elif opt == 5:
            search_crew(name, rank, division, id)
        elif opt == 6:
            filter_by_division(name, division)
        elif opt == 7:
            calculate_payroll(rank)
        elif opt == 8:
            count_officers(rank)
        elif opt == 9:
            print("Exiting program. Goodbye!")
            break
        else:
            print("\n**Invalid option. Please select a valid option from the menu.**")


def init_database():
    '''Initialises the database with default crew members and prompts the user for their name. Returns the lists for names, ranks, divisions, IDs, valid ranks, and the student name.'''
    print("Initializing database...")
    student_name = input("\nEnter Full Name: ")
    print(f"\nWelcome, {student_name.upper()}! \nLoading menu...",)

    name = ["Picard", "Riker", "Data", "Worf", "Spock"]
    rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]
    division = ["Command", "Operations", "Engineering", "Security", "Science"]
    id = [14571, 23331, 34101, 47741, 58921]
    valid_rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]

    return name, rank, division, id, valid_rank, student_name
    

def display_menu():
    '''Displays the menu options to the user and prompts for input. Returns the selected option.'''
    print("\n--- MENU ---")
    print("1. Add Crew")
    print("2. Remove Crew")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")

    try:
        opt = int(input("Select option: "))
    except ValueError:
        opt = 0  
    print(f"\nProceeding with option {opt}...\n")
    return opt

def add_member(name, rank, division, id, valid_rank):
    '''Add a crew member to the lists. User must enter a unique ID and a valid rank to add the crew member to the lists.'''
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_div = input("Division: ")
    new_id = int(input("ID: "))

    while new_id in id:
        print("ID already exists. Please enter a unique ID.")
        new_id = int(input("ID: "))

    while new_rank not in valid_rank:
        print("Invalid rank. Valid ranks are: ")
        for r in valid_rank:
            print("- " + r)
        new_rank = input("Rank: ")

    name.append(new_name)
    rank.append(new_rank)
    division.append(new_div)
    id.append(new_id)

    print("Crew member added.")


def remove_member(name, rank, division, id):
    '''Remove a crew member by their ID. User must enter a valid ID to remove the corresponding crew member from all lists. Uses index search to find the index of the crew member in the lists, then uses pop to remove the crew member from all lists.'''
    remove = int(input("Enter ID of crew member to remove: "))

    if remove in id:
        idx = id.index(remove) 
        name.pop(idx) 
        rank.pop(idx)
        division.pop(idx)
        id.pop(idx)
        print("Crew member removed.")
    else:
        print("ID not found.")


def update_rank(rank, id):
    '''Update the rank of a crew member by their ID. User must enter a valid ID and a new rank.'''
    update = int(input("Enter ID of crew member to update rank: "))

    while update not in id: # If the ID entered by the user is not found in the id list, it will prompt the user to enter a valid ID until a valid ID is entered.
        print("ID not found. Please enter a valid ID.")
        update = int(input("Enter ID of crew member to update rank: "))
        
    idx = id.index(update)
    new_rank = input("New Rank: ")
    rank[idx] = new_rank # Update the rank of the crew member at the index found by the ID search with the new rank entered by the user.
    print("Rank updated.")


def display_roster(name, rank, division, id):
    '''Displaying roster in a table like format with headers and spacing'''
    print("NAME                 RANK                      DIVISION        ID")
    print("-------------------------------------------------------------------------")
    
    for i in range(len(name)):
        print(f"{name[i]:20} {rank[i]:25} {division[i]:15} {id[i]}") # Using spacing e.g :25, to have 25 spaces to align data for table like format


def search_crew(name, rank, division, id):
    '''Search for crew members by name, matches any input with a name in the list.'''
    search = input("Enter name to search: \n").lower()
    found = False

    for i in range(len(name)):
        if search in name[i].lower():
            print(f"{name[i]}, {rank[i]}, {division[i]}, ID: {id[i]}") # Displaying formatted details of each crew member found in search
            found = True
    if not found:
        print("Crew member not found.")


def filter_by_division(name, division):
    '''Filter crew members by division. User must enter Command, Operations, or Sciences.'''
    search = input("Enter division (Command, Operations, or Sciences): ")

    while search not in ["Command", "Operations", "Sciences"]:
        print("Invalid division. Please enter Command, Operations, or Sciences.")
        search = input("Enter division (Command, Operations, or Sciences): ")
    
    found = False
    for i in range(len(division)): # Loops through division list to find matches with user input, if match found, display name and division of crew member
        if division[i] == search:
            print(f"Name: {name[i]}, {division[i]}")
            found = True
    if not found:
            print("No crew members found in that division.")


def calculate_payroll(rank):
    '''Counts number of each rank and multiplies by salary for each rank, then adds together for total payroll.'''
    value = 0

    for r in rank:
        if r == "Captain":
            print("Captain found. \n Adding £80,000 to payroll.")
            value = value + 80000
        elif r == "Commander":
            print("Commander found. \n Adding £60,000 to payroll.")
            value = value + 60000
        elif r == "Lieutenant Commander":
            print("Lieutenant Commander found. \n Adding £50,000 to payroll.")
            value = value + 50000
        elif r == "Lieutenant":
            print("Lieutenant found. \n Adding £40,000 to payroll.")
            value = value + 40000
        elif r == "Science Officer":
            print("Science Officer found. \n Adding £45,000 to payroll.")
            value = value + 45000

    print(f"Total payroll: £{value}")


def count_officers(rank):
    '''Counts and displays number of Commanders and Captains in the crew list.'''
    count = 0
    for r in rank:
        if r == "Commander" or r == "Captain":
            count = count + 1
    print(f"Number of Commanders and Captains: {count}")

main()