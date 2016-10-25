commands = ["new applicant", "help", "veiw applicant"]
applicants = []
names = []
ages = []
positions = []
outline = [names, ages, positions]

database_read = open('programdata.dat', 'r')
def reindex():
    database_read = open('programdata.dat', 'w+')
    database_append = open('programdata.dat', 'a')
    print(applicants)
    #database_append.write("\n".join(applicants))
def command():
    cmd = raw_input("Enter new command: ")
    class CMD:
        if cmd == "new applicant":
            name_input = raw_input("Name: ")
            names.append(name_input.lower())
                
            age_input = raw_input("Age (Must be a whole number): ")
            ages.append(age_input)
                
            position_input = raw_input("Position: ")
            positions.append(position_input.lower())

            for app in outline:
                app = app.split()
                print(app)
            applicants.append(outline)

        elif cmd == "help":
            print("The available commands are: \n")
            for c in commands:
                print(c)
            print("\n")

        elif cmd == "view applicant":
            reindex()
            print(database_read.read())
        else:
            print("Command not found. Try again.")
while(True):
    command()


