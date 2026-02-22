name = ["Picard", "Riker", "Data", "Worf", "Spock"]
rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]
division = ["Command", "Operations", "Engineering", "Security", "Science"]
id = [14571, 23331, 34101, 47741, 58921]

def main():
    print("Welcome to Fleet Manager System")
    init_database()
    display_menu()

def init_database():
    print("Initializing database...")
    
    for i in range(len(name)):
        print(name[i] + " - " + rank[i] + " - " + division[i] + " - ID: " + str(id[i])) 

def display_menu():
    student_name = input("Enter Full Name: ")

    print(f"Welcome, {student_name.upper()}!")
    print("\n--- MENU ---")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Analyze Data")
    print("5. Exit")

    opt = int(input("Select option: "))
    confirm = input(f"You selected option {opt}. Is that correct? (Y/N) ").upper()
    
    while confirm == "Y":
        print(f"Proceeding with option {opt}")      
    else:
        print("Operation cancelled.")
        display_menu()

main()
