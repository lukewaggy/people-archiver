class ListGetter:
    
    def __init__(self):
        self.database = []

    def get_list(self, fileName):
        with open(fileName, 'r') as f:
            print(f.read())