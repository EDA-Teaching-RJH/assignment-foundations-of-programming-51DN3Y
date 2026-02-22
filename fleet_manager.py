def main():
    print("Welcome to Fleet Manager System")
    name, rank, division, id, valid_rank = init_database() 
    display_menu(name, rank, division, id, valid_rank)
    add_member(name, rank, division, id, valid_rank)
    remove_member(name, rank, division, id)

def init_database():
    print("Initializing database...")

    name = ["Picard", "Riker", "Data", "Worf", "Spock"]
    rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]
    division = ["Command", "Operations", "Engineering", "Security", "Science"]
    id = [14571, 23331, 34101, 47741, 58921]
    valid_rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]

    return name, rank, division, id, valid_rank
    
def display_menu(name, rank, division, id, valid_rank):
    student_name = input("Enter Full Name: ")

    print(f"Welcome, {student_name.upper()}!")
    print("\n--- MENU ---")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Analyze Data")
    print("5. Exit")

    opt = int(input("Select option: "))
    print(f"Proceeding with option {opt}")  

    if opt == 1:
        print("Viewing crew...")
    elif opt == 2:
        add_member(name, rank, division, id, valid_rank)
    elif opt == 3:
        remove_member(name, rank, division, id)


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

#def update_rank(name, rank, id):

#def display_roster(name, rank, division, id):
    #for i in range(len(name)):
        #print(name[i] + " - " + rank[i] + " - " + division[i] + " - ID: " + str(id[i])) 

#def search_crew(name, rank, division, id):

#def filter_by_division(name, division):

#def calculate_payroll(rank):

#def count_officers(rank):

main()