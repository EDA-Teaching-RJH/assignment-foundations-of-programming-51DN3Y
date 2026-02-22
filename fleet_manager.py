def main():
    print("Welcome to Fleet Manager System")
    init_database()
    display_menu()

def init_database():
    print("Initializing database...")

    name = ["Picard", "Riker", "Data", "Worf", "Spock"]
    rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]
    division = ["Command", "Operations", "Engineering", "Security", "Science"]
    id = [14571, 23331, 34101, 47741, 58921]

    return (name, rank, division, id)
    
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
    print(f"Proceeding with option {opt}")  


#def add_member(name, rank, division, id):

#def remove_member(name, rank, division, id):

#def update_rank(name, rank, id):

#def display_roster(name, rank, division, id):
    #for i in range(len(name)):
        #print(name[i] + " - " + rank[i] + " - " + division[i] + " - ID: " + str(id[i])) 

#def search_crew(name, rank, division, id):

#def filter_by_division(name, division):

#def calculate_payroll(rank):

#def count_officers(rank):

main()