import os

class ListGetter:
    
    def __init__(self):
        self.database = []

    def get_list(self, fileName):
        if os.path.exists(fileName):   
            print("Previous database found.")
        else:
            open(fileName, 'w')

        with open(fileName, 'r') as f:
            print(f.read())