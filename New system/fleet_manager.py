name = ["Picard", "Riker", "Data", "Worf", "Spock"]
rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Science Officer"]
division = ["Command", "Operations", "Engineering", "Security", "Science"]
id = [14571, 23331, 34101, 47741, 58921]

def main():
    print("Welcome to Fleet Manager System")
    init_database()

def init_database():
    print("Initializing database...")
    
    for i in range(len(name)):
        print(name[i] + " - " + rank[i] + " - " + division[i] + " - ID: " + str(id[i])) 


main()
