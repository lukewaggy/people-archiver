from listgetter import ListGetter
from newapplicant import NewApplicant
from viewapplicant import ViewApplicant
from removeapplicant import RemoveApplicant

def start():
    command = input("Hi, this is the people archiver, please type 'new', 'view', or 'remove': ")
    print(command)

start()