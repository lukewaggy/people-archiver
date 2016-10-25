from listgetter import ListGetter
from newapplicant import NewApplicant
from viewapplicant import ViewApplicant
from removeapplicant import RemoveApplicant

def start():
    
    commands = [NewApplicant(), ViewApplicant(), RemoveApplicant()]
    db = ListGetter()
    db.get_list("database.txt")
    
    print("Welcome to the people archiver.")
    while(True):
        userInput = input("Please type 'new', 'view', or 'remove': ")
        for cmd in commands:
            if cmd.name == userInput:
                cmd.execute()
        

start()