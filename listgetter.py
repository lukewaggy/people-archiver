import os

class ListGetter:
    
    def __init__(self):
        self.database = []

    def get_list(self, fileName):

        # check to see if our database file is there or not
        if os.path.exists(fileName):   
            print("Previous database found.")
        else:
            # else create a new text file named fileName
            open(fileName, 'w')

        populate_list()

    def populate_list(self):
        pass