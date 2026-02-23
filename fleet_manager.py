def main():
    print("\nWelcome to Fleet Manager System")
    name, rank, division, id, valid_rank, student_name = init_database() 
    display_menu(name, rank, division, id, valid_rank, student_name)


def init_database():
    print("Initializing database...")
    student_name = input("\nEnter Full Name: ")
    print(f"\nWelcome, {student_name.upper()}! \nLoading menu...",)

    name = ["Picard", "Riker", "Data", "Worf", "Spock"]
    rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]
    division = ["Command", "Operations", "Engineering", "Security", "Science"]
    id = [14571, 23331, 34101, 47741, 58921]
    valid_rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]

    return name, rank, division, id, valid_rank, student_name
    

def display_menu(name, rank, division, id, valid_rank, student_name):
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

    opt = int(input("Select option: "))
    print(f"\nProceeding with option {opt}...\n")  

    while opt != 9:
        if opt == 1:
            add_member(name, rank, division, id, valid_rank)
            display_menu(name, rank, division, id, valid_rank, student_name)
        elif opt == 2:
            remove_member(name, rank, division, id)
            display_menu(name, rank, division, id, valid_rank, student_name)
        elif opt == 3:
            update_rank(rank, id)
            display_menu(name, rank, division, id, valid_rank, student_name)
        elif opt == 4:
            display_roster(name, rank, division, id)
            display_menu(name, rank, division, id, valid_rank, student_name)
        elif opt == 5:
            search_crew(name, rank, division, id)
            display_menu(name, rank, division, id, valid_rank, student_name)
        elif opt == 6:
            filter_by_division(name, division)
            display_menu(name, rank, division, id, valid_rank, student_name)
        elif opt == 7:
            calculate_payroll(rank)
            display_menu(name, rank, division, id, valid_rank, student_name)
        elif opt == 8:
            count_officers(rank)
            display_menu(name, rank, division, id, valid_rank, student_name)
        else:
            print("\n**Invalid option. Please select a valid option from the menu.**")
            display_menu(name, rank, division, id, valid_rank, student_name)
    
    print("Exiting Program, Goodbye!")
    
    

def add_member(name, rank, division, id, valid_rank):
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
    update = int(input("Enter ID of crew member to update rank: "))

    while update not in id:
        print("ID not found. Please enter a valid ID.")
        update = int(input("Enter ID of crew member to update rank: "))
        
    idx = id.index(update)
    new_rank = input("New Rank: ")
    rank[idx] = new_rank
    print("Rank updated.")


def display_roster(name, rank, division, id):
    print("NAME                 RANK                      DIVISION        ID")
    print("-------------------------------------------------------------------------")
    
    for i in range(len(name)):
        print(f"{name[i]:20} {rank[i]:25} {division[i]:15} {id[i]}")


def search_crew(name, rank, division, id):
    search = input("Enter name to search: \n").lower()
    found = False

    for i in range(len(name)):
        if search in name[i].lower():
            print(f"{name[i]}, {rank[i]}, {division[i]}, ID: {id[i]}")
            found = True
    if not found:
        print("Crew member not found.")


def filter_by_division(name, division):
    search = input("Enter division (Command, Operations, or Sciences): ")

    while search not in ["Command", "Operations", "Sciences"]:
        print("Invalid division. Please enter Command, Operations, or Sciences.")
        search = input("Enter division (Command, Operations, or Sciences): ")
    
    found = False
    for i in range(len(division)):
        if division[i] == search:
            print(f"Name: {name[i]}, {division[i]}")
            found = True
    if not found:
            print("No crew members found in that division.")

def calculate_payroll(rank):
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
    count = 0
    for r in rank:
        if r == "Commander" or r == "Captain":
            count = count + 1
    print(f"Number of Commanders and Captains: {count}")

main()